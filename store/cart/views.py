from django.shortcuts import redirect, render, get_object_or_404
from shop.models import Book
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import stripe

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(book=book, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            book= book,
            quantity=1,
            cart = cart
        )
        cart_item.save()

    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.book.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'Book Shop - New order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']

            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge = stripe.Charge.create(
                amount = stripe_total,
                currency="eur",
                description=description,
                customer=customer.id
            )
        except stripe.error.CardError as e:
            return false, e


    return render(request, 'cart.html', {'cart_items':cart_items, 'total':total, 'counter':counter,
    'data_key':data_key, 'stripe_total':stripe_total,
    'description':description})

def cart_remove(request, book_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    book = get_object_or_404(Book, id=book_id)
    cart_item = CartItem.objects.get(book=book, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

def full_remove(request, book_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    book = get_object_or_404(Book, id=book_id)
    cart_item = CartItem.objects.get(book=book, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')