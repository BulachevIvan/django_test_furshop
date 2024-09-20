from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from cart.models import CartItem
from catalog.models import Product, Category

class CartDetailViewTests(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(id=50000)
        self.product = Product.objects.create(id=1, name='Тестовая шуба', category_id=20)
        self.category = Category.objects.create(id = 20, name = 'Тестовая категория')
        self.cart_item = CartItem.objects.create(id=30, quantity=2, product_id=self.product.id, user_id=self.user.id)
        self.url = reverse('create-order')

    def test_post(self):
        data = {
            'user_id': self.user.id,
            'client_adress': 'москва новый арбат 14'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
