from django.urls import path
from . import views


app_name='shop'


urlpatterns = [
    path('', views.allBookCat, name='allBookCat'),
    path('<uuid:category_id>/', views.allBookCat, name='books_by_category'),
    path('<uuid:category_id>/<uuid:book_id>/', views.book_detail, name='book_detail'),
     path('new/', views.managerCreateView, name='book_new'),

    

]