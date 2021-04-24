from django.urls import path
from . import views

app_name = 'cart'


urlpatterns = [
    path('add/<slug:book_slug>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<slug:book_slug>/', views.cart_remove, name='cart_remove'),
    path('full_remove/<slug:book_slug>/', views.full_remove, name='full_remove'),
]