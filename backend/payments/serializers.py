from rest_framework import serializers
from payments.models import HistoriquePaiement

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriquePaiement
        fields = [
            'id',
            'utilisateur',
            'montant',
            'methode_paiement',
            'date_paiement',
            'statut'
        ]
        read_only_fields = ['id', 'date_paiement']
