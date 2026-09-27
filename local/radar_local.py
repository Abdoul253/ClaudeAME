"""Radar ETF Halal, version locale.

Lit ton compte IBKR via la passerelle officielle « Client Portal Gateway »
(https://localhost:5000 par défaut) et sert une page mobile qui se met à jour
toutes les 30 secondes.

    python3 radar_local.py            # passerelle IBKR, page sur http://localhost:8765
    python3 radar_local.py --lan      # page accessible depuis ton téléphone (même Wi-Fi)
    python3 radar_local.py --demo     # sans IBKR, données de l'instantané du dépôt

Aucune dépendance : Python 3.9+ seulement. Lecture seule : aucun ordre n'est envoyé.
"""
import argparse
import json
import secrets
import socket
import ssl
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
UNIVERSE = json.loads((ROOT / "data" / "universe.json").read_text(encoding="utf-8"))["etfs"]
SNAPSHOT = json.loads(sorted((ROOT / "data").glob("snapshot-*.json"))[-1].read_text(encoding="utf-8"))
BENCH = {"XLK": 4215230, "SMH": 229725622}
# Champs du snapshot Client Portal : dernier, variation, variation %, achat, vente,
# clôture veille, plus haut / plus bas 52 semaines, rendement du dividende.
FIELDS = "31,82,83,84,86,7741,7293,7294,7287"

STATE = {"mode": "init", "updated": None, "error": None, "account": None, "positions": [], "quotes": {}}
LOCK = threading.Lock()


def num(v):
    if v is None:
        return None
    try:
        return float(str(v).replace(",", "").replace("%", "").lstrip("CH"))
    except ValueError:
        return None


class Gateway:
    def __init__(self, base, cafile):
        self.base = base.rstrip("/")
        host = urlparse(self.base).hostname
        if cafile:
            self.ctx = ssl.create_default_context(cafile=cafile)
        elif host in ("localhost", "127.0.0.1"):
            # La passerelle IBKR tourne sur ta machine avec un certificat auto-signé.
            self.ctx = ssl._create_unverified_context()
        else:
            self.ctx = ssl.create_default_context()
        self.account = None

    def call(self, path, method="GET"):
        req = urllib.request.Request(self.base + path, method=method, headers={"User-Agent": "radar-etf-halal"})
        with urllib.request.urlopen(req, context=self.ctx, timeout=15) as r:
            body = r.read()
        return json.loads(body) if body else None

    def refresh(self):
        auth = self.call("/iserver/auth/status", "POST") or {}
        if not auth.get("authenticated"):
            raise RuntimeError("Passerelle IBKR non connectée : ouvre https://localhost:5000 et connecte-toi.")
        self.call("/iserver/accounts")
        if not self.account:
            accts = self.call("/portfolio/accounts") or []
            self.account = accts[0]["accountId"] if accts else None
        acct = None
        positions = []
        if self.account:
            s = self.call(f"/portfolio/{self.account}/summary") or {}
            amt = lambda k: (s.get(k) or {}).get("amount")
            acct = {"net": amt("netliquidation"), "cash": amt("totalcashvalue")}
            for p in self.call(f"/portfolio/{self.account}/positions/0") or []:
                positions.append({"conid": p.get("conid"), "symbol": p.get("contractDesc") or p.get("ticker"),
                                  "qty": p.get("position"), "value": p.get("mktValue"), "pnl": p.get("unrealizedPnl")})
        conids = [str(e["conid"]) for e in UNIVERSE] + [str(c) for c in BENCH.values()]
        quotes = {}
        for row in self.call(f"/iserver/marketdata/snapshot?conids={','.join(conids)}&fields={FIELDS}") or []:
            quotes[str(row.get("conid"))] = {
                "p": num(row.get("31")), "chg": num(row.get("83")), "bid": num(row.get("84")), "ask": num(row.get("86")),
                "prior": num(row.get("7741")), "h52": num(row.get("7293")), "l52": num(row.get("7294")), "dy": num(row.get("7287")),
            }
        return acct, positions, quotes

    def tickle(self):
        try:
            self.call("/tickle", "POST")
        except Exception:
            pass


def demo_state():
    quotes = {}
    for e in UNIVERSE:
        s = SNAPSHOT["snap"].get(e["t"], {})
        quotes[str(e["conid"])] = {"p": s.get("p"), "chg": s.get("chg"), "h52": s.get("h52"), "l52": s.get("l52"), "dy": s.get("dy")}
    return {"net": None, "cash": None}, [], quotes


def poller(gw, demo, every):
    n = 0
    while True:
        try:
            acct, positions, quotes = demo_state() if demo else gw.refresh()
            with LOCK:
                # Le premier appel au snapshot IBKR renvoie souvent des champs vides : on garde la dernière valeur connue.
                for k, q in quotes.items():
                    old = STATE["quotes"].get(k, {})
                    STATE["quotes"][k] = {f: (q.get(f) if q.get(f) is not None else old.get(f)) for f in set(q) | set(old)}
                STATE.update(mode="demo" if demo else "live", updated=time.time(), error=None, account=acct, positions=positions)
        except (urllib.error.URLError, OSError, RuntimeError, ValueError, KeyError) as exc:
            with LOCK:
                STATE.update(error=str(exc))
        n += 1
        if gw and n % 2 == 0:
            gw.tickle()
        time.sleep(every)


class Handler(BaseHTTPRequestHandler):
    token = None

    def log_message(self, *a):
        pass

    def send(self, code, body, ctype):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path in ("/", "/index.html"):
            return self.send(200, (Path(__file__).parent / "mobile.html").read_bytes(), "text/html; charset=utf-8")
        if u.path == "/api/state":
            if self.token and parse_qs(u.query).get("t", [""])[0] != self.token:
                return self.send(401, b'{"error":"code d\'acc\xc3\xa8s manquant"}', "application/json")
            with LOCK:
                payload = dict(STATE, universe=[{k: e[k] for k in ("t", "conid", "cls", "zone", "ter", "debtMax")} for e in UNIVERSE], bench=BENCH)
            return self.send(200, json.dumps(payload).encode(), "application/json")
        self.send(404, b"introuvable", "text/plain")


def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def main():
    ap = argparse.ArgumentParser(description="Radar ETF Halal, version locale")
    ap.add_argument("--gateway", default="https://localhost:5000/v1/api", help="adresse de la passerelle IBKR Client Portal")
    ap.add_argument("--cafile", help="certificat de la passerelle, si tu en as installé un")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--lan", action="store_true", help="accessible depuis le téléphone sur le même Wi-Fi (protégé par un code)")
    ap.add_argument("--every", type=int, default=30, help="secondes entre deux lectures IBKR")
    ap.add_argument("--demo", action="store_true", help="sans IBKR, avec l'instantané du dépôt")
    a = ap.parse_args()

    gw = None if a.demo else Gateway(a.gateway, a.cafile)
    threading.Thread(target=poller, args=(gw, a.demo, a.every), daemon=True).start()
    host = "0.0.0.0" if a.lan else "127.0.0.1"
    if a.lan:
        Handler.token = secrets.token_urlsafe(8)
        print(f"Sur ton téléphone (même Wi-Fi) : http://{lan_ip()}:{a.port}/#t={Handler.token}")
        print("Garde ce lien pour toi : il donne accès aux données de ton compte.")
    else:
        print(f"Ouvre http://localhost:{a.port}")
    ThreadingHTTPServer((host, a.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
