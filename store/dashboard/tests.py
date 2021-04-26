from django.test import TestCase, SimpleTestCase
from django.urls import *
from dashboard.models import *
from dashboard.views import *
from shop.views import managerCreateView


# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_book_new_url_resolved(self):
            url = reverse('dashboard:book_new')
            print(resolve(url).func)
            self.assertEquals(resolve(url).func, managerCreateView)

    def test_manager_dashboard_url_resolved(self):
            url = reverse('dashboard:manager_dashboard')
            print(resolve(url).func)
            self.assertEquals(resolve(url).func, manager_dashboard)

    def test_all_orders_url_resolved(self):
            url = reverse('dashboard:all_orders')
            print(resolve(url).func)
            self.assertEquals(resolve(url).func, orders_list)

    def test_user_list_url_resolved(self):
            url = reverse('dashboard:user_list')
            print(resolve(url).func)
            self.assertEquals(resolve(url).func, userListView)

    def test_voucher_list_url_resolved(self):
            url = reverse('dashboard:voucher_list')
            print(resolve(url).func)
            self.assertEquals(resolve(url).func, voucherListView)

                
    def test_voucher_add_url_resolved(self):
            url = reverse('dashboard:voucher_add')
            print(resolve(url).func)
            self.assertEquals(resolve(url).func, voucherCreateView)

    def test_voucher_edit_url_resolved(self):
            url = reverse('dashboard:voucher_edit', args=['1'])
            print(resolve(url).func)
            self.assertEquals(resolve(url).func, voucherEditView)

    def test_voucher_delete_url_resolved(self):
            url = reverse('dashboard:voucher_delete', args=['1'])
            print(resolve(url).func)
            self.assertEquals(resolve(url).func, voucherDeleteView)

class TestViews(TestCase):
    def test_manager_dashboard_view(self):
        response = self.client.get(reverse('dashboard:manager_dashboard'))
        self.assertEquals(response.status_code,302)
    
    def test_orders_list_view(self):
        response = self.client.get(reverse('dashboard:all_orders'))
        self.assertEquals(response.status_code,302)

    def test_userListView_view(self):
        response = self.client.get(reverse('dashboard:user_list'))
        self.assertEquals(response.status_code,302)