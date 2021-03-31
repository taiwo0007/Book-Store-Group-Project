from django.urls import path
from .views import manager_dashboard, orders_list, reportsView, sales_report, userListView
from shop.views import managerCreateView

app_name = 'dashboard'

urlpatterns = [
    path('', manager_dashboard, name='manager_dashboard'),
    path('new/', managerCreateView, name='book_new'),
    path('all_orders/', orders_list, name='all_orders'),
    path('reports/', reportsView, name='reportsView'),
    path('sales/', sales_report, name='sales_report'),
    path('users/', userListView, name='user_list'),
]
