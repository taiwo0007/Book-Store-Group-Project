from django.urls import path
from . import views


app_name='shop'


urlpatterns = [
    path('', views.allBookCat, name='allBookCat'),
    path('<uuid:category_id>/', views.allBookCat, name='books_by_category'),
    path('<uuid:category_id>/<uuid:book_id>/', views.book_detail, name='book_detail'),
    path('new/', views.ManagerCreateView.as_view(), name='book_new'),
    path('booksManagerList/', views.BookListView.as_view(), name='book_list'),
    path('<uuid:category_id>/<uuid:book_id>/edit/', views.bookUpdateView, name='book_edit'),
    path('<uuid:category_id>/<uuid:book_id>/delete/',views.bookDeleteView, name='book_delete'),

    

]