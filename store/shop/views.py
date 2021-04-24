from django.shortcuts import render, get_object_or_404
from .models import Category, Book, WishList, Review
from django.urls import reverse_lazy
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .forms import BookForm, ReviewForm, BookRatingForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from django.contrib import messages
from order.models import Order
from accounts.models import CustomUser, UserProfile
from django.core.exceptions import ValidationError
from vouchers.models import Voucher


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
  
    bookCategory = Book.objects.filter(category__slug =category_slug)
    booksInCategory = bookCategory.order_by('?')[:6]

    print(request.POST)
    form = ReviewForm()
    try:
        book = Book.objects.get(category__slug=category_slug, slug=book_slug)
    except Exception as e:
        raise e

    Booker = Book.objects.all()


    rating_form = BookRatingForm()
    ratings = Review.objects.filter(review_item__slug = book_slug)
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    half = False
    for i in ratings:
        if i.rating == 1:
            one = one +1
        if i.rating == 2:
            two = two +1
        if i.rating == 3:
            three = three +1
        if i.rating == 4:
            four = four +1
        if i.rating == 5:
            five = five +1
    try:
        total = (5*five + 4*four + 3*three + 2*two +1*one) / (one +two+three+four+five)
    except ZeroDivisionError as e:
        total = 0

    book.star_rating = total
    book.save()
        
    rounded = round(total)
    print(total)
    print(rounded)
    if total >= 1.5 and total < 2:
        rounded = 1
        half = True
    if total >= 2.5 and total < 3:
        rounded = 2
        half = True
    if total >= 3.5 and total < 4:
        rounded = 3
        half = True
    if total >= 4.5 and total < 5:
        rounded = 4
        half = True
    if total >= 5.0:
        rounded = 5
        half = False
        print("hello")
    
    print(rounded)
    UserImage = UserProfile.objects.all()
    reviewss = Review.objects.filter(review_item__slug=book_slug)
    reviews = reviewss.order_by('-created_date')

    

    
    if half:
        greyStars = 4 - rounded
    else:
        greyStars = 5 - rounded

    print(greyStars)
    print(rounded)

    

    return render(request, 'shop/book.html', {'booksInCategory':booksInCategory, 'book':book,'UserImage':UserImage, 'half':half, 'form':form, 'reviews':reviews, 'rounded':rounded, 'greyStars':greyStars})

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

    vouchers_count = Voucher.objects.count()
    managerCheck = True
    books = Book.objects.all()
    books_count = Book.objects.count()
    orders_count = Order.objects.count()
    users_count = CustomUser.objects.count() 
    books = Book.objects.all().filter(availible=True)
    managerCheck = True
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')

    else:
        form = BookForm()

    return render(request, 'shop/book_new.html', {'form':form,'managerCheck':managerCheck,
            'books_count' : books_count,
        'orders_count' : orders_count,
        'users_count' : users_count,
        'books':books,
        'managerCheck':managerCheck,
        "vouchers_count":vouchers_count
    
    })

@user_passes_test(group_check)
def bookListView(request):
    vouchers_count = Voucher.objects.count()
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
        'managerCheck':managerCheck,
        "vouchers_count":vouchers_count
        }
    return render(request, 'shop/book_list.html', context)

@user_passes_test(group_check)
def bookUpdateView(request, category_slug, book_slug):
    managerCheck = True
    managerCheck = True
    vouchers_count = Voucher.objects.count()
    orders = Order.objects.all()
    books = Book.objects.all()
    books_count = books.count()
    orders_count = orders.count()
    users_count = CustomUser.objects.count()
    book = Book.objects.get(category__slug=category_slug, slug=book_slug)

    form = BookForm(request.POST or None, request.FILES or None , instance = book)
    if form.is_valid():
        print(request.POST)
        form.save()
        return HttpResponseRedirect('/')

    return render(request, 'shop/book_edit.html', {'form':form,'managerCheck':managerCheck,
    "orders" : orders,
        "books" : books,
        "books_count" : books_count,
        "orders_count" : orders_count,
        "users_count" : users_count,
        "vouchers_count":vouchers_count
    
    })

@user_passes_test(group_check)
def bookDeleteView(request, category_slug, book_slug):
    vouchers_count = Voucher.objects.count()
    managerCheck = True
    orders = Order.objects.all()
    books = Book.objects.all()
    books_count = books.count()
    orders_count = orders.count()
    users_count = CustomUser.objects.count()
    book = Book.objects.get(category__slug=category_slug, slug=book_slug)
    
    if request.method =="POST":
        book.delete()
        return HttpResponseRedirect('/')

    return render(request, 'shop/book_delete.html', {'book':book,'managerCheck':managerCheck,
    "orders" : orders,
        "books" : books,
        "books_count" : books_count,
        "orders_count" : orders_count,
        "users_count" : users_count,
         "vouchers_count":vouchers_count
    
    })


@login_required()
def addReview(request, category_slug, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    obj = {}
    if request.method == "POST":
        obj = Review.objects.create(
            subject = request.POST['subject'],
            comment = request.POST['comment'],
            user = request.user, 
            rating=request.POST['rating'],
            review_item=book,
            name = str(request.user),

            
            )
        try:
            obj.full_clean()
            obj.save()
            messages.success(request, "Review has been submitted")
            
            
        except ValidationError as e:
            messages.warning(request, "error please enter rating 1 - 5 ")
            obj.delete()
        
        
    
        
   
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