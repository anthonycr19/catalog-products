from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super(ProductViewSet, self).get_permissions()
