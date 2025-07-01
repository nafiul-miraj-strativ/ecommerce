from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ADMIN = 'admin'
    MANAGER = 'manager'
    CUSTOMER = 'customer'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (CUSTOMER, 'Customer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,default=CUSTOMER)