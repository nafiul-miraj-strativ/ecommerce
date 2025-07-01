from django.urls import path, include

app_name = 'user'
urlpatterns = [
    path('', include('apps.user.api.web.v1.urls')),
]