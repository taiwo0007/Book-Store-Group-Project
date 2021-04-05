from django.test import TestCase, SimpleTestCase
from datetime import datetime
from django.urls import reverse, resolve, reverse_lazy
from shop.models import Category, Author, Book
from shop.views import book_detail, allBookCat
from shop.forms import BookForm
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
    
    def test_book_is_assigned_slug_on_creation(self):
        self.assertEquals(self.Book1.slug, 'title')

    def test_category_is_assigned_slug_on_creation(self):
        self.assertEquals(self.Category1.slug, 'test-category-name')

    # def test_book_detail(self):

    #     response = self.client.get(reverse_lazy('shop:book_detail'))
    #     self.assertEqual(response.status_code,200)
    #     self.assertTemplateUsed(response,'shop/book.html')

    # def test_allBookCat(self):

    #     response = self.client.get(reverse_lazy('shop:allBookCat'))
    #     self.assertEqual(response.status_code,200)
    #     self.assertTemplateUsed(response,'shop/category.html')

"""
  path('', views.allBookCat, name='allBookCat'),
    path('books/<slug:category_slug>/', views.allBookCat, name='books_by_category'),
    path('books/<slug:category_slug>/<slug:book_slug>/', views.book_detail, name='book_detail'),
    path('new/', views.managerCreateView, name='book_new'),
    path('booksManagerList/', views.bookListView, name='book_list'),
    path('books/<slug:category_slug>/<slug:book_slug>/edit/', views.bookUpdateView, name='book_edit'),
    path('books/<slug:category_slug>/<slug:book_slug>/delete/',views.bookDeleteView, name='book_delete'),
    path('books/<slug:category_slug>/<slug:book_slug>/add', views.add_to_wishList, name='add_wishlist'),
    path('wishlists/',views.viewWishList, name='wishList_books'),
    path('books/<slug:book_slug>/delete', views.delete_from_wishList, name='wishList_delete'),
    path('top_rated/', views.topRatedBooks, name='topRatedBooks'),
    path('best_value/', views.cheapBooks, name='cheapBooks'),
    path('books/<slug:category_slug>/<slug:book_slug>/add_review/', views.addReview, name="add_review")
"""

        
class TestUrls(SimpleTestCase):

    def test_allBookCat_url_resolved(self):
        url = reverse('shop:allBookCat')
        #print(resolve(url).func)
        self.assertEquals(resolve(url).func, allBookCat)

    def test_books_by_category_kwags_added_resolved(self):
        url = reverse('shop:books_by_category', args=['5cd2e4fa-5fc8-4701-8d76-f72809e00ecd'])
       # print(resolve(url).func)
        self.assertEquals(resolve(url).func, allBookCat)

    def test_book_detail_kwargs_added_resolved(self):
        url = reverse('shop:book_detail', args=['5cd2e4fa-5fc8-4701-8d76-f72809e00ecd','5cd2e4fa-5fc8-4701-8d76-f72809e00ecd'])
        #print(resolve(url).func)
        self.assertEquals(resolve(url).func, book_detail)


    """
    def test_wishLists_url_resolved(self):
        url = reverse()
    """

class TestViews(TestCase):

    def test_cheapBooks(self):
        response = self.client.get(reverse('shop:cheapBooks'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'shop/book_cheap.html')
    
    def test_topRatedBooks(self):
        response = self.client.get(reverse('shop:topRatedBooks'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'shop/book_rating.html')

    def test_book_detail(self):
        response = self.client.get(reverse('shop:book_detail', args=['Fiction','Circle']))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'shop/book.html')

    def test_add_to_wishList(self):
        response = self.client.get(reverse('shop:add_wishlist',args=['Fiction','Circle']))
        self.assertEqual(response.status_code,302)
    
    def test_delete_from_wishList(self):
        response = self.client.get(reverse('shop:wishList_delete',args=['Circle']))
        self.assertEqual(response.status_code,302)
    
    def test_viewWishList(self):
        response = self.client.get(reverse('shop:wishList_books'))
        self.assertEqual(response.status_code,302)
    
    def test_allBookCat(self):
        response = self.client.get(reverse('shop:allBookCat'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'shop/category.html')
    
    def test_managerCreateView(self):
        response = self.client.get(reverse('shop:book_new'))
        self.assertEqual(response.status_code,302)
    
    def test_bookListView(self):
        response = self.client.get(reverse('shop:book_list'))
        self.assertEqual(response.status_code,302)

    def test_bookUpdateView(self):
        response = self.client.get(reverse('shop:book_edit',args=['Fiction','Circle']))
        self.assertEqual(response.status_code,302)
    
    def test_bookDeleteView(self):
        response = self.client.get(reverse('shop:book_delete', args=['Fiction','Circle']))
        self.assertEqual(response.status_code,302)
    
    def test_addReview(self):
        response = self.client.get(reverse('shop:book_delete', args=['Fiction','Circle']))
        self.assertEqual(response.status_code,302)
      
        

