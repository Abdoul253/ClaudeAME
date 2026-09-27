"""Assemble dashboard/index.html from the template and the data files.

Usage: python3 scripts/build.py [snapshot.json]
"""
import json, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
snap_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else sorted((root / "data").glob("snapshot-*.json"))[-1]
universe = json.loads((root / "data" / "universe.json").read_text())["etfs"]
snap = json.loads(snap_path.read_text())
embed = (
    "const UNIVERSE=" + json.dumps(universe, ensure_ascii=False, separators=(",", ":")) + ";\n"
    "const SNAP=" + json.dumps({k: snap[k] for k in ("asOf", "snap", "weeklyEnd", "weekly")}, separators=(",", ":")) + ";"
)
tpl = (root / "dashboard" / "template.html").read_text()
(root / "dashboard" / "index.html").write_text(tpl.replace("/*__DATA__*/", embed))
print("dashboard/index.html <-", snap_path.name)
