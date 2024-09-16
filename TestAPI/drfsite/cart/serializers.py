from rest_framework import serializers
from .models import CartItem
from catalog.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"

class CartItemRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    product_id = serializers.IntegerField(required=False)
    quantity = serializers.IntegerField(required=False)