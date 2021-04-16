from django.urls import path
from shop import views
from .views import signupView, signinView, signoutView, change_password, dashboardView, profileView

urlpatterns = [
    path('create/', signupView, name='signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signoutView, name='signout'),
    path('password_change/', change_password, name='change_password'),
    path('dashboard/', dashboardView, name='dashboard_view'),
    path('profile/', profileView, name='profile_view'),
]