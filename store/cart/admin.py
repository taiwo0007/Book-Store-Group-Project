from django.contrib import admin
from .models import CartItem
# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['book','cart','quantity']
    list_editable = ['cart','quantity']


admin.site.register(CartItem, CartItemAdmin)
