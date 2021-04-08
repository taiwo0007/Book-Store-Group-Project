from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class UserProfile(models.Model): 
    first_name = models.CharField(max_length=150, default="None", blank=True)
    last_name = models.CharField(max_length=150, default="None", blank=True)
    phone_number = models.CharField(max_length=10, default="9999999999", blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email_address = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='blogs', blank=False, default='accounts/user01.jpeg')
    colour = models.CharField(max_length=20, default="blue")
