from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class CategoryRequestSerializer(serializers.Serializer):
    category_id = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class ProductRequestSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class ProductsRequestSerializer(serializers.Serializer):
    category_id = serializers.IntegerField()
    price_min = serializers.IntegerField(required=False)
    price_max = serializers.IntegerField(required=False)
