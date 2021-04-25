from django.shortcuts import render
from shop.models import Book
from django.db.models import Q

def searchResult(request):
    books = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        books = Book.objects.all().filter(Q(title__contains=query) | Q(publisher__contains=query) | Q(iban__contains=query) | Q(author__first_name__contains=query) | Q(author__last_name__contains=query | Q(category__name__contains=query) | Q(author__full_name__contains=query)))
    return render(request, 'search.html',{'query':query,'books':books})
