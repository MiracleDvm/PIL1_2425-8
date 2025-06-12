from django.db import models
from users.models import Utilisateur

class Trajet(models.Model):
    conducteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    point_depart = models.TextField()
    point_arrivee = models.TextField()
    heure_depart = models.TimeField()
    places_disponibles = models.IntegerField()

    def __str__(self):
        return f"{self.point_depart} → {self.point_arrivee} à {self.heure_depart}"
