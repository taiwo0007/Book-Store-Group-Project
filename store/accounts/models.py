from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
