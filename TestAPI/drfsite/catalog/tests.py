from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from catalog.models import Product, Category

class CatalogDetailViewTests(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.category = Category.objects.create(id=20, name="Тестовая категория")
        self.child_category = Category.objects.create(id = 21, name="Тестовая вложенная категория", parent_id = 20)
        self.product = Product.objects.create(id=1, name='Тестовая шуба', category_id=20)
        self.url_get_product = reverse('product-detail')
        self.url_post = reverse('products-post')
        self.url_categories = reverse('categories-get')

    def test_get(self):
        data = {
            'product_id': self.product.id
        }
        response = self.client.get(self.url_get_product, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.product.id)

    def test_post(self):
        data = {
            'category_id': self.category.id
        }
        response = self.client.post(self.url_post, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['category'], self.category.id)

    def test_get_categories(self):
        data = {
            'category_id': self.child_category.id
        }
        response = self.client.get(self.url_categories, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['parent'], self.category.id)