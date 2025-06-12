from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    email = models.EmailField(unique=True)
    budget_mensuel = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    zones_favorites = models.JSONField(default=list)

    # Définition des choix pour le statut de l'utilisateur
    CONDUCTEUR = 'conducteur'
    PASSAGER = 'passager'
    STATUT_CHOICES = [
        (CONDUCTEUR, 'Conducteur'),
        (PASSAGER, 'Passager'),
    ]
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default=PASSAGER,
        verbose_name="Statut"
    )

    def __str__(self):
        return self.email
