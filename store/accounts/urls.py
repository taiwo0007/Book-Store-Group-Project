from django.urls import path
from shop import views
from .views import signupView, signinView, signoutView, change_password

urlpatterns = [
    path('create/', signupView, name='signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signoutView, name='signout'),
    path('password_change/', change_password, name='change_password'),
]