from rest_framework import serializers

from .models import PizzaMenu

class PizzaMenuSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PizzaMenu 
        fields = '__all__'

    def validate(self, data):
        size = data.get('size')
        price_small = data.get('price_small')
        price_medium = data.get('price_medium')
        price_large = data.get('price_large')

        if size not in ["Small", "Medium", "Large"]:
            raise serializers.ValidationError("Size must be 'Small', 'Medium', or 'Large'.")

        if size == "Small" and price_small is None:
            raise serializers.ValidationError("Price for small pizza must be set.")
        elif size == "Medium" and price_medium is None:
            raise serializers.ValidationError("Price for medium pizza must be set.")
        elif size == "Large" and price_large is None:
            raise serializers.ValidationError("Price for large pizza must be set.")

        return data
