from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

app_name = 'web_v1'
router = DefaultRouter()
router.register(r'', ProductViewSet, basename='product')

urlpatterns = router.urls