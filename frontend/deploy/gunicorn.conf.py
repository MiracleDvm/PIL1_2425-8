# frontend/deploy/gunicorn.conf.py

# L'adresse et le port où Gunicorn écoutera
bind = "0.0.0.0:8000"

# Nombre de workers pour gérer les requêtes simultanées (ajustez selon la capacité de votre serveur)
workers = 4

# Temps d'attente maximum d'une requête avant de terminer le worker (en secondes)
timeout = 120

# Type de worker; "gevent" permet un traitement asynchrone améliorant la gestion des connexions concurrentes
worker_class = "gevent"

# Niveau de log
loglevel = "info"

# Configuration des logs : "-" pour rediriger vers la sortie standard
accesslog = "-"
errorlog = "-"
