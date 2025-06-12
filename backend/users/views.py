from rest_framework import generics
from django.contrib.auth import get_user_model
from.serializers import UtilisateurSerializer

class UtilisateurDetailView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UtilisateurSerializer
