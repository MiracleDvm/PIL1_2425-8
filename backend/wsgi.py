import os
from django.core.wsgi import get_wsgi_application

# Définit les paramètres de configuration du projet
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# Crée l'application WSGI
application = get_wsgi_application()
