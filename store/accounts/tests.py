from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from .models import CustomUser
from accounts.views import *
from accounts.models import *
from django.urls import reverse, resolve, reverse_lazy

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


class TestUrls(SimpleTestCase):

    def test_signup_url_resolved(self):
        url = reverse('signup')
        #print(resolve(url).func)
        self.assertEquals(resolve(url).func, signupView)

    def test_signin_url_resolved(self):
        url = reverse('signin')
       # print(resolve(url).func)
        self.assertEquals(resolve(url).func, signinView)

    def test_signout_url_resolved(self):
        url = reverse('signout')
       # print(resolve(url).func)
        self.assertEquals(resolve(url).func, signoutView)

    def test_change_password_url_resolved(self):
        url = reverse('change_password')
       # print(resolve(url).func)
        self.assertEquals(resolve(url).func, change_password)

