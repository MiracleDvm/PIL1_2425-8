from django.urls import path
from trips.views import TrajetListView

urlpatterns = [
    path("", TrajetListView.as_view(), name="trajet-list"),
]
