from django.shortcuts import render
from shop.models import Book
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from shop.models import *
from vouchers.models import *
from order.models import *
from accounts.models import *

def group_check(user):
    if user.groups.filter(name="Manager").exists() == True:
        return True
    else:
        return False

def searchResult(request):
    books = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        books = Book.objects.all().filter(Q(title__contains=query) | Q(publisher__contains=query) | Q(iban__contains=query) | Q(author__first_name__contains=query) | Q(author__last_name__contains=query) | Q(category__name__contains=query) | Q(author__full_name__contains=query))
    return render(request, 'search.html',{'query':query,'books':books})


@user_passes_test(group_check)
def searchResultManager(request):
    books = None
    query = None

    books_count = Book.objects.count()
    orders_count = Order.objects.count()
    users_count = CustomUser.objects.count()
    vouchers = Voucher.objects.all()
    vouchers_count = vouchers.count()
    
    if 'q' in request.GET:
        query = request.GET.get('q')
        books = Book.objects.all().filter(Q(title__contains=query) | Q(publisher__contains=query) | Q(iban__contains=query) | Q(author__first_name__contains=query) | Q(author__last_name__contains=query) | Q(category__name__contains=query) | Q(author__full_name__contains=query))
    
    
    context = {
           
        'books_count' : books_count,
        'orders_count' : orders_count,
        'users_count' : users_count,
        'vouchers':vouchers,
        'vouchers_count': vouchers_count,
        'query':query,
        'books':books
     
        }
    
    return render(request, 'managerSearch.html',context)