from django.urls import path
from . import views


app_name='shop'


urlpatterns = [
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
    path('books/<slug:category_slug>/<slug:book_slug>/add_review/', views.addReview, name="add_review"),
    path('reviews/',views.reviewList, name="reviewList"),

    

]