from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.user.models import User
from apps.user.permissions import IsAdmin
from .serializers import RegisterSerializer, ManagerSerializer

#Customer self-registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
#Creates managers
class CreateManagerView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAdmin]
