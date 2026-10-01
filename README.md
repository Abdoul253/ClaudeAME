# Radar ETF Halal

Suivi des ETF certifiés charia disponibles sur Interactive Brokers : filtre noté, portefeuille de départ à 1 000 $, comparateur, indicateurs de suivi et veille. L'objectif principal est d'avoir des indicateurs précis, clair et conforme à la sharia en prenant en compte un filtre complet des meilleurs ETF. 

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

## Onglets

Temps réel · Filtre ETF · Portefeuille · Dettes & purification · Tech & IA · ROI Djibouti · Comparer · Alertes IBKR · Indicateurs · Veille · Espace gérant (propriétaire seulement).

- **Dettes** : plafond de dette de chaque méthode d'indice (S&P et Dow Jones 33 % de la capitalisation moyenne, MSCI et FTSE 33,33 % des actifs, AAOIFI 30 %), dette pondérée saisie par le gérant, marge et historique des relevés.
- **Purification** : rendement × ratio de purification, en dollars et en % du montant investi.
- **Tech & IA** : R² des rendements hebdomadaires face à XLK et bêta face à SMH, calculés sur un an de cours IBKR ; proposition automatique de réallocation vers les diversifiants (SPSK, SPRE).
- **ROI Djibouti** : franc arrimé à 177,721 FDJ/USD, retenue US de 30 % sur les dividendes des ETF américains (pas de convention fiscale), frais de virement, commissions, purification, zakat, seuil successoral américain de 60 000 $.
- **Alertes** : création d'alertes de prix dans le compte IBKR de l'utilisateur (`create_alert`).

## Données partagées (location)

La page déclare `db` : la collection `compliance/<ticker>` (dette, purification, poids tech, 5 géants IA, source, date, historique) est lue par tous et modifiable par le seul propriétaire. Les réglages de chaque abonné restent dans son navigateur et, s'il est Contributeur, dans `data/users/<id>/prefs`. Chaque abonné utilise son propre connecteur IBKR : les données de marché ne sont pas redistribuées.

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

## Version mobile

- **Dans l'application Claude** (téléphone) : même lien que l'interface. Sous 720 px de large, la page passe en affichage mobile avec une barre d'onglets en bas (Temps réel, Bilan, Tech & IA, Veille, Plus). Les cours viennent du connecteur IBKR de l'utilisateur, rafraîchis chaque minute et relus au retour dans l'application.
- **En local, sans Claude** : `local/radar_local.py` lit le compte via la passerelle officielle IBKR *Client Portal Gateway* et sert `local/mobile.html`.

```
# 1. Télécharger et lancer la passerelle IBKR (Java), puis se connecter sur https://localhost:5000
# 2. Lancer le radar
python3 local/radar_local.py          # http://localhost:8765 sur l'ordinateur
python3 local/radar_local.py --lan    # lien avec code d'accès pour le téléphone (même Wi-Fi)
python3 local/radar_local.py --demo   # essai sans IBKR
```

Lecture seule : le programme n'envoie aucun ordre. La passerelle IBKR demande une reconnexion environ une fois par jour.

## Bilan quotidien

Une routine claude.ai (« Bilan quotidien ETF Halal ») tourne chaque jour à 7 h 52, heure de Djibouti. Elle lit IBKR, cherche l'actualité tech, IA, taux et finance islamique, écrit `briefs/<date>` et `news/latest` dans la base de l'application, puis envoie le résumé en notification.

## Wiki

Les pages du wiki sont dans `wiki/`. La GitHub Action `.github/workflows/wiki.yml` les publie dans le wiki du dépôt à chaque modification. Le wiki doit être activé et avoir une première page créée à la main (limite de GitHub), après quoi la publication est automatique.
