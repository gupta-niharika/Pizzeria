from rest_framework import serializers
from .models import PizzaMenu, SizePrice

class SizePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizePrice
        fields = '__all__'

class PizzaMenuSerializer(serializers.ModelSerializer):
    size_price = SizePriceSerializer()

    class Meta:
        model = PizzaMenu
        fields = '__all__'
