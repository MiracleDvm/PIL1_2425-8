from rest_framework import generics
from.models import Trajet
from.serializers import TrajetSerializer

class TrajetListView(generics.ListCreateAPIView):
    queryset = Trajet.objects.all()
    serializer_class = TrajetSerializer
