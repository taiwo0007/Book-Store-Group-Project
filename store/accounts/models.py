from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class UserProfile(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email_address = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='blogs', blank=True, default='accounts/user01.jpeg')
    colour = models.CharField(max_length=20, default="blue")
