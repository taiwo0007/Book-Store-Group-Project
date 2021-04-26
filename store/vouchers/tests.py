from django.test import TestCase, SimpleTestCase,Client
from django.urls import reverse, resolve, reverse_lazy
from vouchers.views import *
from vouchers.models import *
# Create your tests here.



class TestUrls(SimpleTestCase):


    def test_apply_url_resolved(self):
        url = reverse('vouchers:apply')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, voucher_apply)

class TestViews(TestCase):

    def test_voucher_apply_views(self):
        
        response = self.client.get(reverse('vouchers:apply'))
        # self.assertEquals(response.status_code,200)
        # self.assertTemplateUsed(response,'cart:cart_detail')
