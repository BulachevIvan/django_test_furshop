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
        self.category = Category.objects.create(id=20, name="Тестовая категория")
        self.product = Product.objects.create(id=1, name='Тестовая шуба', category_id=20)
        self.product_in_cart_item = Product.objects.create(id=2, name='Тест для изменения', category_id=20)
        self.cart_item = CartItem.objects.create(id=30, quantity=2, product_id=self.product_in_cart_item.id, user_id=self.user.id)
        self.url = reverse('cart-cart')

    def test_get(self):
        data = {
            'user_id': self.user.id
        }
        response = self.client.get(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        data = {
            'user_id': self.user.id,
            'product_id': self.product.id,
            'quantity': 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data[0]['user'], self.user.id)
        self.assertEqual(response.data[1]['product']['id'], self.product.id)

    def test_put(self):
        data = {
            'user_id': self.user.id,
            'product_id': self.product.id,
            'quantity': 3
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['user'], self.user.id)
        self.assertEqual(response.data[0]['quantity'], data['quantity'])

    def test_delete(self):
        data = {
            'user_id': self.user.id,
            'product_id': self.product_in_cart_item.id
        }
        response = self.client.delete(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(CartItem.objects.filter(user_id=self.user.id, product_id=self.product_in_cart_item.id).exists())