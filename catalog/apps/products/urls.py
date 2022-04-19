from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

app_name = 'api_products'

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = router.urls
