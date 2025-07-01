from django.urls import path, include

app_name = 'product'
urlpatterns = [
    path('', include('apps.product.api.web.v1.urls')),
]