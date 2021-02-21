from django.shortcuts import render, get_object_or_404
from .models import Category, Book

# Create your views here.

def allBookCat(request, category_id=None):
    c_page = None
    books = None
    if category_id != None:
        c_page = get_object_or_404(Category, id=category_id)
        books = Book.objects.filter(category=c_page, availible=True)
    else:
        books = Book.objects.all().filter(availible=True)

    return render(request, 'shop/category.html', {'category':c_page,'books':books})