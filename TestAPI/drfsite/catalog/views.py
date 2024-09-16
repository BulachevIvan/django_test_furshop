from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render

from catalog.models import Product
from catalog.serializers import ProductSerializer, ProductRequestSerializer, ProductsRequestSerializer, \
    CategoryRequestSerializer, CategorySerializer
from catalog.services import ProductsService


class ProductDetailView(generics.GenericAPIView):

    @swagger_auto_schema(
        operation_summary="Получение информации о конретном продукте",
        manual_parameters=[
            openapi.Parameter('product_id', openapi.IN_QUERY, description='product_id',
                              type=openapi.TYPE_INTEGER, required=True)],
        responses={200: ProductSerializer(), 500: "Серверная ошибка"},
    )
    def get(self, request):
        serializer = ProductRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        product = Product.objects.get(id=serializer.validated_data.get('product_id'))
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductsView(generics.GenericAPIView):

    @swagger_auto_schema(
        operation_summary="Получение списка продуктов",
        request_body=ProductsRequestSerializer(),
        responses={200: ProductSerializer(many=True), 500: "Серверная ошибка"},
    )
    def post(self, request):
        serializer = ProductsRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = ProductsService(**serializer.validated_data)
        data = service.get_products()
        result = ProductSerializer(data, many=True).data
        return Response(result)

class CategorysView(generics.GenericAPIView):

    @swagger_auto_schema(
        operation_summary="Получение категории",
        manual_parameters=[
            openapi.Parameter('category_id', openapi.IN_QUERY, description='category_id',
                              type=openapi.TYPE_INTEGER, required=True)],
        responses={200: CategorySerializer(), 500: "Серверная ошибка"},
    )
    def get(self, request):
        serializer = CategoryRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        service = ProductsService(**serializer.validated_data)
        data = service.get_category()
        result = CategorySerializer(data, many=True).data
        return Response(result)
