from django.shortcuts import render, get_object_or_404
from .models import Category, Book, WishList, Review
from django.urls import reverse_lazy
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .forms import BookForm, ReviewForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from django.contrib import messages
from order.models import Order
from accounts.models import CustomUser


def group_check(user):
    if user.groups.filter(name="Manager").exists() == True:
        return True
    else:
        return False

@login_required()
def reviewList(request):
    reviews = Review.objects.filter(user = request.user)
   
    return render(request, 'shop/reviews.html', {'reviews':reviews})
    

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

def book_detail(request, category_slug, book_slug):
    form = ReviewForm()
   
    reviewss = Review.objects.filter(review_item__slug=book_slug)
    reviews = reviewss.order_by('-created_date')

    print(reviews)
    try:
        book = Book.objects.get(category__slug=category_slug, slug=book_slug)
    except Exception as e:
        raise e

    return render(request, 'shop/book.html', {'book':book, 'form':form, 'reviews':reviews})

@login_required()
def add_to_wishList(request, book_slug, category_slug):
    print(book_slug)
    book = get_object_or_404(Book, slug=book_slug)
    

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
def delete_from_wishList(request, book_slug):
    
    book = WishList.objects.get(wished_item__slug=book_slug, user = request.user)
    book.delete()
    messages.success(request, 'Successfully deleted from Wish List')

    return HttpResponseRedirect('/wishlists/')


@login_required() 
def viewWishList(request):
    managerCheck = False
    books = WishList.objects.filter(user = request.user)
    return render(request, 'shop/wishlist_books.html', {'books':books})

def allBookCat(request, category_slug=None):
    managerCheck = False

    print(category_slug)
    print(category_slug)

    if request.user.groups.filter(name="Manager").exists() == True:
        managerCheck = True

    c_page = None
    books = None
    if category_slug != None:
        c_page = get_object_or_404(Category, slug=category_slug)
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
    books_count = Book.objects.count()
    orders_count = Order.objects.count()
    users_count = CustomUser.objects.count() 
    context = {
        'books_count' : books_count,
        'orders_count' : orders_count,
        'users_count' : users_count,
        'books':books,
        'managerCheck':managerCheck
        }
    return render(request, 'shop/book_list.html', context)

@user_passes_test(group_check)
def bookUpdateView(request, category_slug, book_slug):
    managerCheck = True
    book = Book.objects.get(category__slug=category_slug, slug=book_slug)

    form = BookForm(request.POST or None, request.FILES or None , instance = book)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    return render(request, 'shop/book_edit.html', {'form':form,'managerCheck':managerCheck})

@user_passes_test(group_check)
def bookDeleteView(request, category_slug, book_slug):
    managerCheck = True
    book = Book.objects.get(category__slug=category_slug, slug=book_slug)
    
    if request.method =="POST":
        book.delete()
        return HttpResponseRedirect('/')

    return render(request, 'shop/book_delete.html', {'book':book,'managerCheck':managerCheck})


@login_required()
def addReview(request, category_slug, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    
    if request.method == "POST":
        obj = Review.objects.create(
            subject = request.POST['subject'],
            comment = request.POST['comment'],
            user = request.user, 
            review_item=book,
            name = str(request.user),

            
            )
        obj.save()
        messages.success(request, "Review has been submitted")
    
        
   
    return HttpResponseRedirect(book.get_absolute_url())


   

"""
@login_required()
def add_to_wishList(request, book_slug, category_slug):
    print(book_slug)
    book = get_object_or_404(Book, id=book_slug)
    

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
        form = ReviewForm()

    return render(request, 'shop/book_new.html', {'form':form,'managerCheck':managerCheck})
    """