from django.test import TestCase
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
