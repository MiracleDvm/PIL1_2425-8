from rest_framework import serializers
from.models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'budget_mensuel', 'zones_favorites']
