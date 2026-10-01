# ETF suivis

Les 16 ETF certifiés charia disponibles sur Interactive Brokers que le Radar suit. Ils sont tous dans la watchlist IBKR « ETF Halal ».

| Ticker | Nom | Classe | Type | Frais | Filtre charia | Règle de dette de l'indice |
|---|---|---|---|---|---|---|
| SPUS | SP Funds S&P 500 Sharia Industry Exclusions | Actions US | ETF US | 0,45 % | S&P Shariah (Ratings Intelligence) | Dette < 33 % de la capitalisation moyenne sur 36 mois |
| HLAL | Wahed FTSE USA Shariah | Actions US | ETF US | 0,50 % | FTSE / Yasaar | Dette < 33,33 % des actifs totaux |
| MNZL | Manzil Russell Halal USA Broad Market | Actions US | ETF US | 0,40 % | AAOIFI + droits humains (IdealRatings) | Dette portant intérêt < 30 % de la capitalisation |
| SPWO | SP Funds S&P World ex-US | Actions monde hors US | ETF US | 0,55 % | S&P Shariah | Dette < 33 % de la capitalisation moyenne sur 36 mois |
| UMMA | Wahed Dow Jones Islamic World | Actions monde hors US | ETF US | 0,65 % | DJ Islamic + revue éthique Wahed | Dette < 33 % de la capitalisation moyenne sur 24 mois |
| SPSK | SP Funds Dow Jones Global Sukuk | Sukuk | ETF US | 0,50 % | AAOIFI (sukuk) | Sans objet : titres adossés à des actifs, pas d'actions |
| SPRE | SP Funds S&P Global REIT Sharia | Immobilier | ETF US | 0,50 % | S&P Shariah | Dette < 33 % de la capitalisation moyenne sur 36 mois |
| SPTE | SP Funds S&P Global Technology | Thématique tech | ETF US | 0,55 % | S&P Shariah | Dette < 33 % de la capitalisation moyenne sur 36 mois |
| KWIN | KraneShares Wahed Alternative Income | Revenu alternatif | ETF US | 0,51 % | Wahed (ventes à terme conformes) | Méthode propre au fonds, voir prospectus |
| ISDW | iShares MSCI World Islamic | Actions monde dév. | UCITS IE | 0,30 % | MSCI Islamic | Dette < 33,33 % des actifs totaux |
| HIWS | HSBC MSCI World Islamic Screened | Actions monde dév. | UCITS IE | 0,30 % | MSCI Islamic + ESG | Dette < 33,33 % des actifs totaux |
| MWIM | Invesco MSCI ACWI Islamic M-Series | Actions monde (dév.+EM) | UCITS IE | 0,35 % | MSCI Islamic | Dette < 33,33 % des actifs totaux |
| ISDU | iShares MSCI USA Islamic | Actions US | UCITS IE | 0,30 % | MSCI Islamic | Dette < 33,33 % des actifs totaux |
| SPWI | Wahed S&P 500 Shariah UCITS | Actions US | UCITS IE | 0,49 % | S&P Shariah + revue Wahed | Dette < 33 % de la capitalisation moyenne sur 36 mois |
| ISDE | iShares MSCI EM Islamic | Actions émergentes | UCITS IE | 0,35 % | MSCI Islamic | Dette < 33,33 % des actifs totaux |
| DJIW | Wahed Dow Jones Islamic World UCITS | Actions monde (dév.+EM) | UCITS IE | 0,65 % | DJ Islamic + revue Wahed | Dette < 33 % de la capitalisation moyenne sur 24 mois |

## Accès selon la résidence

- **Résident de l'UE ou de l'EEE** : seuls les ETF UCITS (cotés à Londres) sont achetables. Le règlement PRIIPs interdit les ETF américains aux particuliers, faute de document d'information (KID).
- **Résident de Djibouti ou d'un autre pays hors UE** : les deux familles sont accessibles. Les ETF américains s'achètent par fractions chez IBKR ; les UCITS en parts entières.

## Sources des données

- Cours, performances, volatilité, encours et liquidité : connecteur IBKR (`get_price_snapshot`, `get_price_history`).
- Frais et méthodes d'indice : fiches des émetteurs et justETF (septembre 2026).
- Fichier source : `data/universe.json`.
