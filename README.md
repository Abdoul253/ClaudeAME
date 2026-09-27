# Radar ETF Halal

Suivi des ETF certifiés charia disponibles sur Interactive Brokers : filtre noté, portefeuille de départ à 1 000 $, comparateur, indicateurs de suivi et veille.

Interface publiée : https://claude.ai/artifact/SoGPxuK7eR41qqkQDm7Z2H

## Fonctionnement

- `data/universe.json` : les 16 ETF suivis (ticker, identifiant de contrat IBKR, indice, méthode de filtrage charia, frais, domicile).
- `data/snapshot-AAAA-MM-JJ.json` : instantané IBKR (cours, performances, volatilité, encours, clôtures hebdomadaires sur un an). Sert de repli quand la page n'a pas accès au compte.
- `dashboard/template.html` : l'interface. Ouverte dans Claude avec le connecteur Interactive Brokers (IBKR), elle lit en direct `get_price_snapshot`, `get_price_history`, `get_account_summary` et `get_account_positions` (rafraîchissement toutes les 5 minutes pour les cours, toutes les heures pour l'historique).
- `scripts/build.py` : assemble `dashboard/index.html` à partir du modèle et des données.

```
python3 scripts/build.py            # utilise le dernier instantané
```

Une watchlist IBKR « ETF Halal » contient les mêmes 16 lignes.

## Score du filtre

Filtres éliminatoires : accès selon la résidence (un résident UE/EEE ne peut pas acheter d'ETF américains, règlement PRIIPs), classe d'actifs, encours minimum, frais maximum, liquidité, type de dividendes, historique d'un an.

Score sur 100 des ETF retenus, chaque critère ramené sur 0–1 au sein du groupe : performance prix 1 an (25), performance / volatilité (25), frais (20), taille log (15), liquidité log (15). Pondérations modifiables dans l'interface.

## Portefeuilles de départ

| Profil | Hors UE (ETF US, fractions possibles) | UE / EEE (UCITS, parts entières) |
|---|---|---|
| Prudent | SPUS 45 · SPWO 20 · SPSK 35 | MWIM 70 · liquidités 30 |
| Équilibré | SPUS 55 · SPWO 30 · SPSK 15 | ISDW 80 · ISDE 20 |
| Dynamique | SPUS 65 · SPWO 35 | MWIM 100 |

Outil de suivi, pas un conseil en investissement.
