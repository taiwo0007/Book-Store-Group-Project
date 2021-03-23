from django.urls import path
from . import views


app_name='shop'


urlpatterns = [
    path('', views.allBookCat, name='allBookCat'),
    path('<uuid:category_id>/', views.allBookCat, name='books_by_category'),
    path('<uuid:category_id>/<uuid:book_id>/', views.book_detail, name='book_detail'),
    path('new/', views.managerCreateView, name='book_new'),
    path('booksManagerList/', views.bookListView, name='book_list'),
    path('<uuid:category_id>/<uuid:book_id>/edit/', views.bookUpdateView, name='book_edit'),
    path('<uuid:category_id>/<uuid:book_id>/delete/',views.bookDeleteView, name='book_delete'),
    path('<uuid:category_id>/<uuid:book_id>/add', views.add_to_wishList, name='add_wishlist'),
    path('wishlists/',views.viewWishList, name='wishList_books'),
    path('<uuid:book_id>/delete', views.delete_from_wishList, name='wishList_delete'),
    path('highest_rated/', views.highRatedBooks, name='highRatedBooks'),
    path('best_value/', views.cheapBooks, name='cheapBooks'),

    

]