from rest_framework.views import APIView
from rest_framework.response import Response
from payments.models import HistoriquePaiement

class RemboursementView(APIView):
    def post(self, request, paiement_id):
        paiement = HistoriquePaiement.objects.get(id=paiement_id)
        paiement.statut = "remboursé"
        paiement.save()
        return Response({"message": "Paiement remboursé avec succès."})
