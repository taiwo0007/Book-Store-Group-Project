from django.test import TestCase
from django.contrib.auth import get_user_model
from shop.models import Book, Category, Author
from datetime import datetime
from django.db import models
from django.conf import settings
from .models import Blog
from accounts.models import CustomUser

class TestModels(TestCase):

    def setUp(self):
        self.CustomUser1 = CustomUser.objects.create(
            username='testcustomuser',
            email='testcustomuser@email.com',
            password='secret'
        )
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
            category = self.Category1,  
        )
        self.Blog1 = Blog.objects.create(
            title = 'blogtitle',
            author = self.CustomUser1,
            body = 'Text field',
            book_blog = self.Book1,
            created_date = datetime(2020, 5, 17),
        )


    def test_blog_create_success(self):
        self.assertEqual(f'{self.Blog1.title}', 'blogtitle')
        self.assertEqual(self.Blog1.author, self.CustomUser1)
        self.assertEqual(f'{self.Blog1.body}', 'Text field')
        self.assertEqual(self.Blog1.book_blog, self.Book1)
