from django.urls import path
from .views import *
from shop.views import managerCreateView

app_name = 'dashboard'

urlpatterns = [
    path('', manager_dashboard, name='manager_dashboard'),
    path('new/', managerCreateView, name='book_new'),
    path('all_orders/', orders_list, name='all_orders'),
    path('users/', userListView, name='user_list'), 
    path('voucher_list/', voucherListView, name='voucher_list'),
    path('voucher_add/', voucherCreateView, name='voucher_add'),
    path('voucher_edit/<int:voucher_id>/', voucherEditView, name='voucher_edit'),
    path('voucher_delete/<int:voucher_id>/', voucherDeleteView, name='voucher_delete')
]
