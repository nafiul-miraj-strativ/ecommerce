from django.urls import path
from .views import RegisterView, CreateManagerView

app_name = 'web_v1'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('create-manager/', CreateManagerView.as_view(), name='create_manager'),
]