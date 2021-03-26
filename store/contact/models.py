from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(null=False)
    subject=models.TextField()

    def __str__(self):
        return f'{self.lastname}, {self.firstname}, {self.email}'