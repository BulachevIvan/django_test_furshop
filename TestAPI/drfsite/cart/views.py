from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response

from cart.serializers import CartItemSerializer, CartItemRequestSerializer
from cart.services import CartsService


class CartDetailView(generics.GenericAPIView):

    @swagger_auto_schema(
        operation_summary="Получение списка товаров в корзине",
        manual_parameters=[
            openapi.Parameter('user_id', openapi.IN_QUERY, description='user_id',
                              type=openapi.TYPE_INTEGER, required=True)],
        responses={200: CartItemSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request):
        serializer = CartItemRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        service = CartsService(**serializer.validated_data)
        data = service.get_cart()
        serializer = CartItemSerializer(data, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Добавление товара в корзину",
        request_body=CartItemRequestSerializer(),
        responses={200: CartItemSerializer(many=True), 500: "Серверная ошибка"},
    )
    def post(self, request):
        serializer = CartItemRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = CartsService(**serializer.validated_data)
        data = service.post_item()
        result = CartItemSerializer(data, many=True).data
        return Response(result)

    @swagger_auto_schema(
        operation_summary="Изменение товара",
        request_body=CartItemRequestSerializer(),
        responses={200: CartItemSerializer(many=True), 500: "Серверная ошибка"},
    )
    def put(self, request):
        serializer = CartItemRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = CartsService(**serializer.validated_data)
        data = service.put_item()
        result = CartItemSerializer(data, many=True).data
        return Response(result)

    @swagger_auto_schema(
        operation_summary="Удаление товара из корзины",
        request_body=CartItemRequestSerializer(),
        responses={200: CartItemSerializer(many=True), 500: "Серверная ошибка"},
    )
    def delete(self, request):
        serializer = CartItemRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = CartsService(**serializer.validated_data)
        data = service.delete_item()
        result = CartItemSerializer(data, many=True).data
        return Response(result)