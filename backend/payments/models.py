from django.db import models
from users.models import Utilisateur

class HistoriquePaiement(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    methode_paiement = models.CharField(max_length=20, choices=[("PayPal", "PayPal"), ("Stripe", "Stripe")])
    date_paiement = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=15,
        choices=[("réussi", "Réussi"), ("échoué", "Échoué"), ("remboursé", "Remboursé")],
        default="réussi"
    )

    def __str__(self):
        return f"{self.utilisateur} - {self.montant} €"
