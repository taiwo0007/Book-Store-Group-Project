from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve, reverse_lazy
from voucher.views import *
from .model import *
# Create your tests here.



class TestUrls(SimpleTestCase):


    def test_apply_url_resolved(self):
        url = reverse('vouchers:apply')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, voucher_apply)

