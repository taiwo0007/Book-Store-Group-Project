from django.test import TestCase
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