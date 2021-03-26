from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser

class TestModels(TestCase):

    def setUp(self):
        self.CustomUser1 = CustomUser.objects.create(
            username='testcustomuser',
            email='testcustomuser@email.com',
            password='secret'
        )


    def test_customuser_create_success(self):
        self.assertEqual(f'{self.CustomUser1.username}', 'testcustomuser')
        self.assertEqual(f'{self.CustomUser1.email}', 'testcustomuser@email.com')
        self.assertEqual(f'{self.CustomUser1.password}', 'secret')
