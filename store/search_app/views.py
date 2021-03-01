from django.shortcuts import render
from shop.models import Book
from django.db.models import Q

def searchResult(request):
    books = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        books = Book.objects.all().filter(Q(title__contains=query) | Q(publisher__contains=query))
    return render(request, 'search.html',{'query':query,'books':books})
