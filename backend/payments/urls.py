from django.urls import path
from payments.views import RemboursementView

urlpatterns = [
    path("<int:paiement_id>/rembourser/", RemboursementView.as_view(), name="rembourser-paiement"),
]
