# Version mobile et locale

## Sur téléphone, dans l'application Claude

Ouvre https://claude.ai/artifact/SoGPxuK7eR41qqkQDm7Z2H dans l'application Claude. Sur un écran étroit, la page passe en affichage mobile :

- barre d'onglets en bas : Temps réel, Bilan, Tech & IA, Veille, Plus
- cours lus avec ton propre connecteur IBKR, rafraîchis chaque minute et à chaque retour dans l'application
- heure de la dernière mise à jour affichée en haut

Au premier chargement, Claude demande l'autorisation d'utiliser le connecteur IBKR pour cette page.

## En local, sans passer par Claude

Le programme `local/radar_local.py` lit ton compte par la passerelle officielle d'IBKR (Client Portal Gateway) et sert une page mobile qui se met à jour toutes les 30 secondes. Il ne passe aucun ordre.

1. Télécharge la passerelle Client Portal Gateway sur le site d'IBKR, lance-la, puis connecte-toi sur https://localhost:5000.
2. Lance le radar :

```
python3 local/radar_local.py          # page sur http://localhost:8765
python3 local/radar_local.py --lan    # lien avec code d'accès pour le téléphone (même Wi-Fi)
python3 local/radar_local.py --demo   # essai sans IBKR
```

3. Avec `--lan`, ouvre sur le téléphone le lien affiché (il contient un code d'accès). Ajoute-le à l'écran d'accueil.

Il faut Python 3.9 ou plus récent, sans autre dépendance. La passerelle IBKR demande une reconnexion environ une fois par jour.
