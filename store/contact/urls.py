from django.urls import path
from shop import views
from .views import contactView



urlpatterns = [
    path('', contactView, name='contact'),
]