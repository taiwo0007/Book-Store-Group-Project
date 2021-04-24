from django.urls import path
from .views import manager_dashboard, orders_list, userListView
from shop.views import managerCreateView

app_name = 'dashboard'

urlpatterns = [
    path('', manager_dashboard, name='manager_dashboard'),
    path('new/', managerCreateView, name='book_new'),
    path('all_orders/', orders_list, name='all_orders'),
    path('users/', userListView, name='user_list'), 
]
