from rest_framework import generics

from .models import PizzaMenu 
from .serializers import PizzaMenuSerializer

class PizzaListView(generics.ListAPIView):
    queryset = PizzaMenu.objects.all() 
    serializer_class = PizzaMenuSerializer
    pagination_class = None 

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
