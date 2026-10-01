# Bilan quotidien

Chaque matin, deux routines claude.ai préparent un bilan et l'envoient en notification sur le téléphone.

| Heure (Djibouti) | Routine | Rôle |
|---|---|---|
| 7 h 40 | Relevé IBKR du matin | Lit le compte IBKR (solde, positions, alertes) et les cours des 16 ETF, plus XLK et SMH, puis les dépose dans l'application (`market/latest`) |
| 7 h 52 | Bilan quotidien ETF Halal | Reprend ce relevé, cherche l'actualité tech, IA, taux et finance islamique, écrit le bilan (`briefs/<date>`) et la veille (`news/latest`), puis envoie la notification |

Le relevé de 7 h 40 tourne dans la session Claude reliée au compte IBKR : il ne faut pas archiver cette session. Le bilan signale « Relevé IBKR du matin absent » si le relevé a plus de 3 heures.

## Contenu du bilan

- Titre du jour
- 3 à 6 constats chiffrés : compte, ETF, tech et IA, taux
- Points à surveiller dans la journée (séance américaine de 16 h 30 à 23 h, heure de Djibouti)
- Tableau des cours, variations du jour et depuis janvier

Les sept derniers bilans sont dans l'onglet Bilan ; le dernier s'affiche en haut de l'onglet Temps réel.

## Si le bilan n'arrive pas

1. Vérifie que le connecteur Interactive Brokers (IBKR) est connecté sur https://claude.ai/customize/connectors.
2. Vérifie dans la page des routines de claude.ai que les deux routines sont actives.
3. Ouvre l'application : l'onglet Veille indique l'heure de la dernière mise à jour.
