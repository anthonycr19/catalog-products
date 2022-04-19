from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group
from apps.users.models import User
from .models import Product


class ProductModelTest(TestCase):
    def test_sku_length(self):
        product = Product.objects.create(
            name='celular',
            price=180,
            brand='xiaomi'
        )
        self.assertEqual(len(product.sku), Product.SKU_LENGTH)

    def test_sku_random_not_custom(self):
        sku_custom = '123456789012345'
        product = Product.objects.create(
            sku=sku_custom,
            name='celular',
            price=180,
            brand='xiaomi'
        )
        self.assertNotEqual(product.sku, sku_custom)

    def test_sku_custom_update(self):
        """
        - sku random only create
        - custom sku when edit
        """
        sku_custom = '123456789012345'
        product = Product.objects.create(
            name='celular',
            price=180,
            brand='xiaomi'
        )
        product.sku = sku_custom
        product.save()
        self.assertEqual(product.sku, sku_custom)


class ProductApiTest(APITestCase):
    def create_user(self):
        group = Group.objects.create(name='admin')
        user = User.objects.create_user(username='admin', password='peru2022')
        group.user_set.add(user)

    def setUp(self):
        self.create_user()
        login = {
            "username": "admin",
            "password": "peru2022"
        }
        response = self.client.post('/api/v1/auth/sign-in/', data=login)
        self.token = response.data['token']

    def test_create_product(self):
        product_data = {
          "name": "celular",
          "price": 180,
          "brand": "xiaomi"
        }
        response = self.client.post('/api/v1/products/', data=product_data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get("name"), product_data.get("name"))
        self.assertEqual(response.data.get("price"), product_data.get("price"))
        self.assertEqual(response.data.get("brand"), product_data.get("brand"))

    def test_get_detail_product(self):
        product_data = {
            "name": "celular",
            "price": 180,
            "brand": "xiaomi"
        }
        product = Product.objects.create(**product_data)
        product_data["sku"] = product.sku
        response = self.client.get(
            f'/api/v1/products/{product.sku}/',
            HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )
        self.assertEqual(response.data, product_data)
