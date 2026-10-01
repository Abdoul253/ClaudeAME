# Questions fréquentes

**Les cours sont-ils à jour ?**
Dans l'application ouverte dans Claude, oui : ils viennent de ton connecteur IBKR et se rafraîchissent chaque minute. Hors de Claude, la page affiche l'instantané du 25/09/2026.

**Pourquoi « IBKR indisponible » ?**
Le connecteur n'est pas autorisé pour la page ou a expiré. Reconnecte-le sur https://claude.ai/customize/connectors, puis clique sur Actualiser.

**Pourquoi SPUS et HLAL ensemble ne diversifient pas ?**
Leur corrélation hebdomadaire sur un an est de 0,96 : ils font doublon. Garde-en un seul.

**Comment réduire la dépendance à la tech ?**
Dans l'onglet Tech & IA, fixe un plafond. La page propose de déplacer du poids vers les sukuk (SPSK) ou l'immobilier (SPRE), qui ne suivent presque pas la tech.

**Les performances incluent-elles les dividendes ?**
Non. Ce sont des variations de prix. Les dividendes sont affichés à part (colonne Div.).

**L'application passe-t-elle des ordres ?**
Non. Elle lit le compte et peut créer des alertes de prix si tu le demandes. Aucun ordre n'est envoyé.

**Comment mettre à jour l'instantané de secours ?**
Ajoute un fichier `data/snapshot-AAAA-MM-JJ.json`, puis lance `python3 scripts/build.py`.
