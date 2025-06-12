from django.urls import path
from reservations.views import ReservationListView, AnnulerReservationView

urlpatterns = [
    path("", ReservationListView.as_view(), name="reservations"),
    path("<int:pk>/delete/", AnnulerReservationView.as_view(), name="annuler-reservation"),
]
