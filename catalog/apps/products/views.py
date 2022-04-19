from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer
from .decorators import user_read_porduct


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @user_read_porduct
    def retrieve(self, request, *args, **kwargs):
        return super(ProductViewSet, self).retrieve(request, *args, **kwargs)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
