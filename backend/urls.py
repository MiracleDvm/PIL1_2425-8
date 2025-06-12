from django.contrib import admin
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Vue d'accueil minimale
def home(request):
    return JsonResponse({"message": "Bienvenue sur l'API IFRI Comotorage"})

# Vue d'accueil qui redirige vers le build Vue.js (index.html)
def home_redirect(request):
    return HttpResponseRedirect('/static/index.html')

# Debug view to log static file requests
def static_debug(request, path):
    print(f"[DEBUG] Static debug hit: {path}")
    return HttpResponse(f"Static debug: {path}")

urlpatterns = [
    path('', home_redirect, name='home-redirect'),
    path('admin/', admin.site.urls),  # Interface d'administration Django
    path('api/trips/', include('trips.urls')),  # Routes API pour les trajets
    path('api/payments/', include('payments.urls')),  # Routes API pour les paiements
    path('api/reservations/', include('reservations.urls')),  # Routes API pour les réservations
    path('api/users/', include('users.urls')),  # Routes API pour les utilisateurs
    path('api/notifications/', include('notifications.urls')),  # Routes API pour les notifications
    path('api/auth/', include('authentication.urls')),  # Routes API pour l'authentification
    path('api/monitoring/', include('monitoring.urls')),  # Surveillance et logs
    path('static/test-debug/<path:path>', static_debug),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
