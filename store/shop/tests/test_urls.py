from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import allBookCat, book_detail


class TestUrls(SimpleTestCase):

    def test_allBookCat_url_functional(self):
        url = reverse('allBookCat')
        self.assertEquals(resolve(url).func, allBookCat)


    