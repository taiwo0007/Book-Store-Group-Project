from django.shortcuts import render, get_object_or_404
from .models import Category, Book, WishList
from django.urls import reverse_lazy
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .forms import BookForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from django.contrib import messages
def group_check(user):
    if user.groups.filter(name="Manager").exists() == True:
        return True
    else:
        return False

# Create your views here.

def cheapBooks(request):

    booksCheapF = Book.objects.filter(category='b6e303f8-d681-4aa2-ab8a-ad3b27a62015')
    booksCheapFiction = booksCheapF.order_by('price')[:6]

    booksCheapC= Book.objects.filter(category='1a8c0bf6-85cf-4170-ab6b-45604dd43cf2')
    booksCheapChildren = booksCheapC.order_by('price')[:6]

    booksCheapN= Book.objects.filter(category='f1b46f0d-7ee6-4ecb-a649-aaeb6407f836')
    booksCheapNon = booksCheapN.order_by('price')[:6]

    for i in booksCheapChildren:
        print(i.price)

    for l in booksCheapFiction:
        print(l.price)
    
    for j in booksCheapNon:
        print(j.price)



    return render(request, 'shop/book_cheap.html', {'booksCheapChildren':booksCheapChildren, 'booksCheapFiction':booksCheapFiction,'booksCheapNon':booksCheapNon })


def topRatedBooks(request):

    booksPopulateF = Book.objects.filter(category='b6e303f8-d681-4aa2-ab8a-ad3b27a62015')
    booksRatedFiction = booksPopulateF.order_by('-star_rating')[:6]

    booksPopC= Book.objects.filter(category='1a8c0bf6-85cf-4170-ab6b-45604dd43cf2')
    booksRatedChildren = booksPopC.order_by('-star_rating')[:6]

    booksPopN= Book.objects.filter(category='f1b46f0d-7ee6-4ecb-a649-aaeb6407f836')
    booksRatedNon = booksPopN.order_by('-star_rating')[:6]

    for i in booksRatedChildren:
        print(i.star_rating)

    for l in booksRatedFiction:
        print(l.star_rating)
    
    for j in booksRatedNon:
        print(j.star_rating)



    return render(request, 'shop/book_rating.html', {'booksRatedChildren':booksRatedChildren, 'booksRatedFiction':booksRatedFiction,'booksRatedNon':booksRatedNon })

def book_detail(request, category_id, book_id):

    try:
        book = Book.objects.get(category_id=category_id, id=book_id)
    except Exception as e:
        raise e

    return render(request, 'shop/book.html', {'book':book})

@login_required()
def add_to_wishList(request, book_id, category_id):
    print(book_id)
    book = get_object_or_404(Book, id=book_id)
    

    try :
        obj = WishList.objects.get(user=request.user, wished_item=book)
        messages.warning(request, 'Item already added in wishlist ')
        
    except WishList.DoesNotExist:
        obj = WishList.objects.create(
            user = request.user, 
            wished_item=book,
        )
        obj.save()
        messages.success(request,'"' +str(obj.wished_item) +'" added to Wish List')
   
    return HttpResponseRedirect(book.get_absolute_url())

@login_required()
def delete_from_wishList(request, book_id):
    
    book = WishList.objects.get(wished_item_id=book_id, user = request.user)
    book.delete()
    messages.success(request, 'Successfully deleted from Wish List')

    return HttpResponseRedirect('/wishlists/')


@login_required() 
def viewWishList(request):
    managerCheck = False
    books = WishList.objects.filter(user = request.user)
    return render(request, 'shop/wishlist_books.html', {'books':books})

def allBookCat(request, category_id=None):
    managerCheck = False

    if request.user.groups.filter(name="Manager").exists() == True:
        managerCheck = True

    c_page = None
    books = None
    if category_id != None:
        c_page = get_object_or_404(Category, id=category_id)
        books = Book.objects.filter(category=c_page, availible=True) 
    else:
        books = Book.objects.all().filter(availible=True)
    
    paginator = Paginator(books,24)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        books = paginator.page(page)
    except (EmptyPage,InvalidPage):
        books = paginator.page(paginator.num_pages)


   
    

    return render(request, 'shop/category.html', {'category':c_page,'books':books,'managerCheck':managerCheck })

@user_passes_test(group_check)
def managerCreateView(request):
    
    books = Book.objects.all().filter(availible=True)
    managerCheck = True
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')

    else:
        form = BookForm()

    return render(request, 'shop/book_new.html', {'form':form,'managerCheck':managerCheck})

@user_passes_test(group_check)
def bookListView(request):
    managerCheck = True
    books = Book.objects.all()
    return render(request, 'shop/book_list.html',{'books':books,'managerCheck':managerCheck})

@user_passes_test(group_check)
def bookUpdateView(request, category_id, book_id):
    managerCheck = True
    book = Book.objects.get(category_id=category_id, id=book_id)

    form = BookForm(request.POST or None, request.FILES or None , instance = book)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    return render(request, 'shop/book_edit.html', {'form':form,'managerCheck':managerCheck})

@user_passes_test(group_check)
def bookDeleteView(request, category_id, book_id):
    managerCheck = True
    book = Book.objects.get(category_id=category_id, id=book_id)
    
    if request.method =="POST":
        book.delete()
        return HttpResponseRedirect('/')

    return render(request, 'shop/book_delete.html', {'book':book,'managerCheck':managerCheck})
