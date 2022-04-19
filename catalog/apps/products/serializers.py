from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """product model serializer"""

    class Meta:
        model = Product
        fields = ('sku', 'name', 'price', 'brand')
        extra_kwargs = {
            'sku': {'read_only': True}
        }
