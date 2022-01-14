from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class BuyItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()

    def validate_quantity(self, quantity):
        if quantity <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return quantity