from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from search_app.views import searchResult



class TestUrls(SimpleTestCase):

    def test_searchResult_url_resolved(self):
            url = reverse('search_app:searchResult')
            print(resolve(url).func)
            self.assertEquals(resolve(url).func, searchResult)

