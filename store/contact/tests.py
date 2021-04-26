from django.test import TestCase, SimpleTestCase
from . models import Contact
from contact.views import *
from django.urls import reverse, resolve, reverse_lazy
from . models import Contact

class TestModels(TestCase):

    def setUp(self):
        self.Contact1 = Contact.objects.create(
            firstname = 'firstname',
            lastname = 'lastname',
            email = 'thisemail@email.com',
            subject = 'this is the subject',
        )

    def test_contact_create_success(self):
        self.assertEqual(f'{self.Contact1.firstname}', 'firstname')
        self.assertEqual(f'{self.Contact1.lastname}', 'lastname')
        self.assertEqual(f'{self.Contact1.email}', 'thisemail@email.com')
        self.assertEqual(f'{self.Contact1.subject}', 'this is the subject')


class TestUrls(SimpleTestCase):
    def test_contact_url_resolved(self):
        url = reverse('contact')
        print(resolve(url).func)
        # self.assertEquals(resolve(url).func, contactView)

class TestViews(TestCase):

    def test_ContactView_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'contact.html')