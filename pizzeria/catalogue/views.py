from rest_framework import generics

from .models import PizzaMenu
from .serializers import PizzaMenuSerializer

class PizzaMenuListView(generics.ListAPIView):
    queryset = PizzaMenu.objects.all()
    serializer_class = PizzaMenuSerializer
