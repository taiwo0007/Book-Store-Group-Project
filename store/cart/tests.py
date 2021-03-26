from django.test import TestCase
from datetime import datetime
from shop.models import Category, Author, Book
from .models import Cart, CartItem


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
        self.Cart1 = Cart.objects.create(
            cart_id = 'cartid',
            date_added = datetime(2020, 5, 16),
        )
        self.CartItem1 = CartItem.objects.create(
            book = self.Book1,
            cart = self.Cart1,
            quantity = 2,
            active = 'True'
        )
        
    def test_cart_create_success(self):
        self.assertEqual(f'{self.Cart1.cart_id}', 'cartid')

    def test_cart_item_create_success(self):
        self.assertEqual(self.CartItem1.book, self.Book1)
        self.assertEqual(self.CartItem1.cart, self.Cart1)
        self.assertEqual(self.CartItem1.quantity, 2)
        self.assertTrue(self.CartItem1.active)