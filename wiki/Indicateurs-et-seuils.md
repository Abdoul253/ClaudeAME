# Indicateurs et seuils

Chaque indicateur a un seuil qui doit déclencher une action. Les valeurs se lisent dans l'onglet indiqué.

## Dettes et conformité

| Indicateur | Ce qu'il mesure | Seuil d'alerte | Où le lire |
|---|---|---|---|
| Dette pondérée vs plafond | Ratio de dette moyen des sociétés du fonds face au plafond de son indice | Plus de 80 % du plafond utilisé | Dettes & purification |
| Tendance de la dette | Évolution d'un relevé à l'autre | Trois hausses de suite | Dettes & purification |
| Certification | Comité charia ou indice islamique reconnu | Retrait ou changement d'indice | Site de l'émetteur |

Plafonds de dette par méthode d'indice :

| Méthode | Règle |
|---|---|
| S&P Shariah, Dow Jones Islamic | Dette < 33 % de la capitalisation moyenne (36 ou 24 mois) |
| MSCI Islamic, FTSE / Yasaar | Dette < 33,33 % des actifs totaux |
| AAOIFI (MNZL) | Dette portant intérêt < 30 % de la capitalisation |

## Épuration

| Indicateur | Ce qu'il mesure | Seuil d'alerte |
|---|---|---|
| Ratio de purification | Part des dividendes à donner en charité | Au-delà de 5 % des dividendes |
| Taux d'épuration sur l'investi | Rendement du dividende × ratio de purification | À verser à chaque dividende |
| Intérêts sur liquidités | Intérêts versés par IBKR sur le cash (riba) | Tout intérêt crédité : désactiver dans les paramètres du compte |

## Performance, liquidité, rendement

| Indicateur | Seuil d'alerte |
|---|---|
| Performance 1 mois, depuis janvier, 1 an (prix, hors dividendes) | 5 points sous l'ETF du même segment |
| Liquidité (volume moyen 90 jours, écart achat/vente) | Volume < 250 k$/jour ou écart > 0,30 % |
| Rendement du dividende | Baisse de moitié |
| Baisse maximale sur un an | Au-delà de 15 % sur le portefeuille |

## Dépendance à la tech et à l'IA

| Indicateur | Ce qu'il mesure | Seuil d'alerte |
|---|---|---|
| Dépendance tech (R² face à XLK) | Part des variations expliquée par la tech américaine | Au-dessus du plafond fixé (0,60 par défaut) |
| Bêta puces IA (face à SMH) | Réaction aux semi-conducteurs | Au-dessus de 0,40 |
| Poids des 5 géants de l'IA | Nvidia, Apple, Microsoft, Alphabet, Broadcom | Au-delà de 40 % |

Mesures sur un an de cours IBKR au 26/09/2026 : SPUS 0,86, HLAL 0,82, SPWO 0,55, ISDW 0,60, SPSK 0,13, SPRE 0,03.

## Score du filtre

Les ETF qui passent les filtres éliminatoires reçoivent une note sur 100. Chaque critère est ramené sur 0–1 au sein du groupe puis pondéré (pondérations modifiables) : performance 1 an 25, performance / volatilité 25, frais 20, taille 15, liquidité 15.
