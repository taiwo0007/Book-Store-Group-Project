from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserProfileForm, CustomUserChangeForm
from shop.models import WishList, Review
from order.forms import RefundForm
from order.models import Order
from blog.forms import BlogForm
from blog.models import Blog
from .models import CustomUser, UserProfile
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required()
def profileView(request):
    rForm = RefundForm()
    pForm = PasswordChangeForm(request.user)
    blogform = BlogForm()
    blog = Blog.objects.filter(author=request.user)
    p = UserProfile.objects.get(user=request.user)
    totalW = WishList.objects.all()
    totalO = Order.objects.all()
    totalR = Review.objects.all()
    wishlist = WishList.objects.filter(user=request.user)
    orders = Order.objects.filter(emailAddress = request.user.email)
    reviews = Review.objects.filter(user=request.user)
    form = UserProfileForm(instance = p)
    form2 = CustomUserChangeForm(instance=request.user)
      

    
    if request.method == 'POST':
       print(request.POST)
       form = UserProfileForm(request.POST, request.FILES, instance = p)
       if form.is_valid():
           form.save()
           messages.success(request,'Your pofile has been updated!')
    
    context = {
        'totalR':totalR,
        'totalO':totalO,
        'totalW':totalW,
        'p':p,
        'wishlist' :wishlist,
        'reviews':reviews,
        'orders':orders,
        'form':form,
        'form2': form2,
        'blogform':blogform,
        'blog':blog,
        'pForm':pForm,
        'rForm':rForm
      

    }
    
    return render(request, 'profile.html', context)


@login_required()
def dashboardView(request):

    try:
        wishlist = WishList.objects.filter(user=request.user)
    except WishList.DoesNotExist:
        wishlist = 0
    
    try:
        orders = Order.objects.filter(emailAddress = request.user.email)
    except Order.DoesNotExist: 
        orders = 0
    
    try:
        reviews = Review.objects.filter(user=request.user)
    except Review.DoesNotExist:
        reviews = 0
    context = {
        'wishlist' :wishlist,
        'reviews':reviews,
        'orders':orders
    }

   
    return render(request, 'dashboard_profile.html', context)

def signupView(request):

    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(CustomUser.objects.raw("SELECT email FROM accounts WHERE username = {}".format(username)))
            signup_user = CustomUser.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
            print(signup_user)

            obj = UserProfile.objects.create(
                user = signup_user,
                email_address = form.cleaned_data.get('email')
            )
            obj.save()
            print(obj)

    else:
        form = CustomUserCreationForm()


    return render(request, 'signup.html', {'form':form})         

def signinView(request):



    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    obj = UserProfile.objects.get(user=user, email_address = user.email)
        
                except UserProfile.DoesNotExist:
                    obj = UserProfile.objects.create(
                    user = user,
                    email_address = user.email
                    )
                    obj.save()
                    
                print("----------------------------------------------hello worled")
                return redirect('shop:allBookCat')
            else:
                print("=============================================hello worled")
                return redirect('signup')

            
    else:
        form = AuthenticationForm()

       
    return render(request, 'signin.html', {'form':form})   



def signoutView(request):
    logout(request)
    return redirect('signin')

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('signin')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })