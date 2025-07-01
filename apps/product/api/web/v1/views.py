from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.product.models import Product
from apps.product.permissions import IsManager
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsManager()]