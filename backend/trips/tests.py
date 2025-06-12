from django.test import TestCase
from trips.models import Trajet
from users.models import Utilisateur

class TrajetTestCase(TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur.objects.create(username="testuser", email="test@example.com")
        self.trajet = Trajet.objects.create(
            conducteur=self.utilisateur,
            point_depart="Paris",
            point_arrivee="Lyon",
            heure_depart="12:00",
            places_disponibles=3
        )

    def test_trajet_creation(self):
        self.assertEqual(self.trajet.point_depart, "Paris")
        self.assertEqual(self.trajet.conducteur, self.utilisateur)
