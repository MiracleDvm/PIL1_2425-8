from rest_framework import serializers
from.models import Trajet

class TrajetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajet
        fields = ['id', 'conducteur', 'point_depart', 'point_arrivee', 'heure_depart', 'places_disponibles']
