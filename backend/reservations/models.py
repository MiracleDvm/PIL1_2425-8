from django.db import models
from users.models import Utilisateur
from trips.models import Trajet

class Reservation(models.Model):
    passager = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=15,
        choices=[("en attente", "En attente"), ("confirmé", "Confirmé"), ("annulé", "Annulé")],
        default="en attente"
    )

    def __str__(self):
        return f"Réservation de {self.passager} pour {self.trajet}"
