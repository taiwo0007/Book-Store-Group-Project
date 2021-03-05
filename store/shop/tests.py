from django.test import TestCase
from datetime import datetime
from django.urls import reverse
from shop.models import Category, Author, Book
import uuid

class TestModels(TestCase):

    def setUp(self):
        self.Category1 = Category.objects.create(
            name = 'Test category name',
            description = 'Test description',
            popularity = 5
        )
        self.Author1 = Author.objects.create(
            first_name = 'Test author f name',
            last_name = 'Test author l name',
            age = 25,
            about = 'Test about field'
        )
        self.Book1 = Book.objects.create(
            iban = 'IFG4565',
            title = 'Title',
            synopsis = 'Synopsis',
            price = 5.0,
            star_rating = 5,
            stock = 10,
            availible = True,
            created = datetime(2020, 5, 17),
            updated = datetime(2020, 5, 18),
            pub_date = datetime(2020, 5, 16),
            num_pages = 50,
            publisher = 'Publisher',
            author = self.Author1,
            category = self.Category1  
        )
        

    def test_category_create_success(self):
        self.assertEqual(self.Category1.id, self.Category1.id)
        self.assertEqual(f'{self.Category1.name}', 'Test category name')
        self.assertEqual(f'{self.Category1.description}', 'Test description')
        self.assertEqual(self.Category1.popularity, 5)

    def test_author_create_success(self):
        self.assertEqual(self.Author1.id, self.Author1.id)
        self.assertEqual(f'{self.Author1.first_name}', 'Test author f name')
        self.assertEqual(f'{self.Author1.last_name}', 'Test author l name')
        self.assertEqual(self.Author1.age, 25)
        self.assertEqual(f'{self.Author1.about}', 'Test about field')

    def test_book_create_success(self):
        self.assertEqual(self.Book1.id, self.Book1.id)
        self.assertEqual(f'{self.Book1.iban}', 'IFG4565')
        self.assertEqual(f'{self.Book1.title}', 'Title')
        self.assertEqual(f'{self.Book1.synopsis}', 'Synopsis')
        self.assertEqual(self.Book1.price, 5.0)
        self.assertEqual(self.Book1.star_rating, 5)
        self.assertEqual(self.Book1.stock, 10)
        self.assertTrue(self.Book1.availible)
        self.assertEqual(self.Book1.created, self.Book1.created)
        self.assertEqual(self.Book1.updated, self.Book1.updated)
        self.assertEqual(self.Book1.pub_date, self.Book1.pub_date)
        self.assertEqual(self.Book1.num_pages, 50)
        self.assertEqual(f'{self.Book1.publisher}', 'Publisher')
        self.assertEqual(self.Book1.author, self.Author1)
        self.assertEqual(self.Book1.category, self.Category1)

        
    