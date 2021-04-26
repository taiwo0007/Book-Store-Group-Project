from django.test import TestCase, SimpleTestCase
from datetime import datetime
from django.urls import *
from shop.models import Category, Author, Book
from shop.views import book_detail, allBookCat
import uuid
from shop.views import *
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
    


    #Slugiffied
    def test_books_by_category_url_resolved(self):
        url = reverse('shop:books_by_category', args=['childrens'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, allBookCat)

    def test_book_detail_url_resolved(self):
        url = reverse('shop:book_detail', args=['childrens', 'diary-of-a-wimpy-kid'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, book_detail)

    def test_book_new_url_resolved(self):
        url = reverse('shop:book_new')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, managerCreateView)

    def test_book_list_url_resolved(self):
        url = reverse('shop:book_list')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, bookListView)

    def test_book_edit_url_resolved(self):
        url = reverse('shop:book_edit', args=['childrens', 'diary-of-a-wimpy-kid'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, bookUpdateView)

    def test_book_delete_url_resolved(self):
        url = reverse('shop:book_delete', args=['childrens', 'diary-of-a-wimpy-kid'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, bookDeleteView)

    def test_add_wishList_url_resolved(self):
        url = reverse('shop:add_wishlist', args=['childrens', 'diary-of-a-wimpy-kid'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, add_to_wishList)

    def test_wishList_books_url_resolved(self):
        url = reverse('shop:wishList_books')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, viewWishList)

    def test__wishList_delete_url_resolved(self):
        url = reverse('shop:wishList_delete', args=['diary-of-a-wimpy-kid'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, delete_from_wishList)

    def test__topRatedBooks_url_resolved(self):
        url = reverse('shop:topRatedBooks')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, topRatedBooks)

    def test_cheapBooks_url_resolved(self):
        url = reverse('shop:cheapBooks')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, cheapBooks)
    
    def test_add_review_url_resolved(self):
        url = reverse('shop:add_review', args=['childrens', 'diary-of-a-wimpy-kid'])
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, addReview)

    def test_reviewList_url_resolved(self):
        url = reverse('shop:reviewList')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, reviewList)

class TestViews(TestCase):

    def test_reviewList_views(self):
        response = self.client.get(reverse('shop:reviewList')) 
        self.assertEquals(response.status_code,302)
        # self.assertTemplateUsed(response,'shop/reviews.html')
    
    def test_cheapBooks_views(self):
        response = self.client.get(reverse('shop:cheapBooks'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop/book_cheap.html')
    
    def test_topRatedBooks_views(self):
        response = self.client.get(reverse('shop:topRatedBooks'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop/book_rating.html')
    
    # def test_book_detail_views(self):

    #     response = self.client.get(reverse('shop:book_detail',args=['childrens', 'diary-of-a-wimpy-kid']))
    #     self.assertEquals(response.status_code,200)

    def test_viewWishList_views(self):
        response = self.client.get(reverse('shop:wishList_books'))
        self.assertEquals(response.status_code,302)

    def test_allBookCat_views(self):
        response = self.client.get(reverse('shop:books_by_category',args=['fiction']))
        self.assertEquals(response.status_code,404)

    
    def test_managerCreateView_view(self):
        response = self.client.get(reverse('shop:book_new'))
        self.assertEquals(response.status_code,302)
    
    def test_bookListView_view(self):
        response = self.client.get(reverse('shop:book_list'))
        self.assertEquals(response.status_code,302)
    
    # def test_bookUpdateView_view(self):
    #     response = self.client.get(reverse('shop:book_edit'))
    #     self.assertEquals(response.status_code,302)