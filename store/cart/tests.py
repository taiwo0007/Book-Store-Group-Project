from django.test import TestCase, SimpleTestCase
from datetime import datetime
from shop.models import Category, Author, Book
from .models import Cart, CartItem
from .models import *
from cart.views import *
from django.urls import reverse, resolve, reverse_lazy

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



class TestUrls(SimpleTestCase):

    def test_add_cart_url_resolved(self):
        url = reverse('cart:add_cart', args=['diary-of-a-wimpy-kid'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, add_cart)
    

    def test_cart_detail_url_resolved(self):
        url = reverse('cart:cart_detail')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, cart_detail)

    def test_cart_remove_url_resolved(self):
        url = reverse('cart:cart_remove',args=['diary-of-a-wimpy-kid'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, cart_remove)

    def test_full_remove_url_resolved(self):
        url = reverse('cart:full_remove', args=['diary-of-a-wimpy-kid'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, full_remove)
    
class TestViews(TestCase):

    def test_add_cart_view(self):
        pass
        # response = self.client.get(reverse('cart:add_cart',args=['diary-of-a-wimpy-kid']))
        # self.assertEquals(response.status_code,302)
        # self.assertTemplateUsed(response,'cart:cart_detail')
    
    
