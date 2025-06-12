from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from.views import UtilisateurDetailView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('user/', UtilisateurDetailView.as_view(), name='user-detail'),
]
