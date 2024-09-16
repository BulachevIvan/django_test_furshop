from django.shortcuts import render
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from order.serializers import OrderRequestSerializer, OrderSerializer
from order.services import OrderService


class OrderView(generics.GenericAPIView):
    @swagger_auto_schema(
        operation_summary="Создание заказа",
        request_body=OrderRequestSerializer(),
        responses={200: OrderSerializer(many=True), 500: "Серверная ошибка"},
    )
    def post(self, request):
        serializer = OrderRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = OrderService(**serializer.validated_data)
        data = service.create_order()
        result = OrderSerializer(data, many=True).data
        return Response(result)

