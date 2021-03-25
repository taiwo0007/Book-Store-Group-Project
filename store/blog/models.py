from django.db import models
from django.urls import reverse
from django.conf import settings
from shop.models import Book

# Create your models here.


class Blog(models.Model):   
    title = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.CharField(max_length=1040)
    image = models.ImageField(upload_to='blogs', blank=True, default='blo01.png')
    book_blog = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
