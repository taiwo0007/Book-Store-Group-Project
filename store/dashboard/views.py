from django.shortcuts import render
from django.http import HttpResponse
from vouchers.models import Voucher
from order.models import Order, OrderItem
from shop.models import Book
from accounts.models import CustomUser
from accounts.forms import UserChangeForm
from django.db.models import Sum, DecimalField, Count, IntegerField
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.functions import Cast
from shop.views import group_check
from datetime import datetime
from django.http import HttpResponseRedirect
from vouchers.forms import VoucherForm
from django.urls import reverse






@user_passes_test(group_check)
def manager_dashboard(request):
    vouchers = Voucher.objects.all()
    vouchers_count = vouchers.count()
    
    orders = Order.objects.all()
    books = Book.objects.all()
    books_count = books.count()
    orders_count = orders.count()
    users_count = CustomUser.objects.count()
    total_sales = Order.objects.aggregate(my_sum=Cast(Sum('total'), IntegerField()))
    this_month = datetime.now().month
    today = datetime.now().day
    this_month_sales = Order.objects.filter(created__month=this_month).aggregate(my_sum=Cast(Sum('total'), IntegerField()))
    todays_sales = Order.objects.filter(created__day=today).aggregate(my_sum=Cast(Sum('total'), IntegerField()))
    jan_sales = Order.objects.filter(created__lt='2021-01-31').filter(created__gt='2021-01-01').count()
    feb_sales = Order.objects.filter(created__lt='2021-02-28').filter(created__gt='2021-02-01').count()
    march_sales = Order.objects.filter(created__lt='2021-03-31').filter(created__gt='2021-03-01').aggregate(my_sum=Cast(Sum('total'), DecimalField()))
    april_sales = Order.objects.filter(created__lt='2021-04-30').filter(created__gt='2021-04-01').aggregate(my_sum=Cast(Sum('total'), DecimalField()))
    may_sales = Order.objects.filter(created__lt='2021-05-31').filter(created__gt='2021-05-01').count()
    june_sales = Order.objects.filter(created__lt='2021-06-30').filter(created__gt='2021-06-01').count()
    july_sales = Order.objects.filter(created__lt='2021-07-31').filter(created__gt='2021-07-01').count()
    aug_sales = Order.objects.filter(created__lt='2021-08-31').filter(created__gt='2021-08-01').count()
    sep_sales = Order.objects.filter(created__lt='2021-09-30').filter(created__gt='2021-09-01').count()
    oct_sales = Order.objects.filter(created__lt='2021-10-31').filter(created__gt='2021-10-01').count()
    nov_sales = Order.objects.filter(created__lt='2021-11-30').filter(created__gt='2021-11-01').count()
    dec_sales = Order.objects.filter(created__lt='2021-12-31').filter(created__gt='2021-12-01').count()

    
    context = {
        "orders" : orders,
        "books" : books,
        "vouchers_count": vouchers_count,
        "books_count" : books_count,
        "orders_count" : orders_count,
        "users_count" : users_count,
        'total_sales':total_sales,
        'this_month_sales' : this_month_sales,
        'todays_sales' : todays_sales,
        "jan_sales" : jan_sales,
        "feb_sales" : feb_sales,
        "march_sales" : march_sales,
        "april_sales" : april_sales,
        "may_sales" : may_sales,
        "june_sales" : june_sales,
        "july_sales" : july_sales,
        "aug_sales" : aug_sales,
        "sep_sales" : sep_sales,
        "oct_sales" : oct_sales,
        "nov_sales" : nov_sales,
        "dec_sales" : dec_sales,
    }
    return render(request, "dashboard/manager_dashboard.html", context)

@user_passes_test(group_check)
def orders_list(request):
    orders = Order.objects.all()
    books_count = Book.objects.count()
    orders_count = Order.objects.count()
    users_count = CustomUser.objects.count()
    vouchers = Voucher.objects.all()
    vouchers_count = vouchers.count()
    context = {
        "orders" : orders,
        'books_count' : books_count,
        'orders_count' : orders_count,
        'users_count' : users_count,
        "vouchers_count": vouchers_count,
        }
    return render(request, "dashboard/order_list.html", context)

@user_passes_test(group_check)
def userListView(request):
    vouchers = Voucher.objects.all()
    vouchers_count = vouchers.count()
    users = CustomUser.objects.all()
    books_count = Book.objects.count()
    orders_count = Order.objects.count()
    users_count = CustomUser.objects.count()
    context = {
     
        'users':users,
        'books_count' : books_count,
        'orders_count' : orders_count,
        'users_count' : users_count,
         "vouchers_count": vouchers_count,
        }
    return render(request, 'dashboard/user_list.html', context)


""""""   """   """   """   """   """   """   """   """   """   """   """   """   """   """   """   """   """    """

@user_passes_test(group_check)
def voucherCreateView(request):


    books_count = Book.objects.count()
    orders_count = Order.objects.count()
    users_count = CustomUser.objects.count()
    vouchers = Voucher.objects.all()
    vouchers_count = vouchers.count()
    if request.method == 'POST':
        form = VoucherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard:voucher_list'))

    else:
        form = VoucherForm()

    return render(request, 'dashboard/voucher_add.html', {'form':form,
   
        'books_count' : books_count,
        'orders_count' : orders_count,
        'users_count' : users_count,
         "vouchers_count": vouchers_count,
    
    
    
    
    })

@user_passes_test(group_check)
def voucherListView(request):

    
    books_count = Book.objects.count()
    orders_count = Order.objects.count()
    users_count = CustomUser.objects.count()
    vouchers = Voucher.objects.all()
    vouchers_count = vouchers.count()
    context = {
           
        'books_count' : books_count,
        'orders_count' : orders_count,
        'users_count' : users_count,
        'vouchers':vouchers,
        'vouchers_count': vouchers_count,
     
        }
    return render(request, 'dashboard/voucher_list.html', context)

@user_passes_test(group_check)
def voucherEditView(request, voucher_id):
  
    books_count = Book.objects.count()
    orders_count = Order.objects.count()
    users_count = CustomUser.objects.count()
    vouchers = Voucher.objects.all()
    vouchers_count = vouchers.count()
    voucher = Voucher.objects.get(id=voucher_id)

    form = VoucherForm(request.POST or None , instance = voucher)
    if form.is_valid():
        print(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('dashboard:voucher_list'))

    return render(request, 'dashboard/voucher_edit.html', {'form':form,
    
        "books_count" : books_count,
        "orders_count" : orders_count,
        "users_count" : users_count,
        "vouchers_count": vouchers_count,
    
    })

@user_passes_test(group_check)
def voucherDeleteView(request, voucher_id):

    books_count = Book.objects.count()
    orders_count = Order.objects.count()
    users_count = CustomUser.objects.count()
    vouchers = Voucher.objects.all()
    vouchers_count = vouchers.count()
    voucher = Voucher.objects.get(id=voucher_id)
    
    if request.method =="POST":
        voucher.delete()
        return HttpResponseRedirect(reverse('dashboard:voucher_list'))

    return render(request, 'dashboard/voucher_delete.html', {'voucher':voucher,
    
        "books_count" : books_count,
        "orders_count" : orders_count,
        "users_count" : users_count,
        "vouchers_count": vouchers_count,
    
    })

