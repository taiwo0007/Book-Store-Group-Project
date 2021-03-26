from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve, reverse_lazy
from search_app.views import searchResult




class TestUrls(SimpleTestCase):

    def test_searchResult_url_resolved(self):
        url = reverse('search_app:searchResult')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, searchResult)

class searchResultsTest(TestCase):

    def test_searchResult(self):
        response = self.client.get(reverse_lazy('search_app:searchResult'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'search.html')
