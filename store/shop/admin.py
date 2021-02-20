from django.contrib import admin
from .models import Category, Book


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['iban', 'title', 'synopsis', 'price', 'star_rating', 'stock', 'availible', 'created', 'updated', 'pub_date', 'num_pages', 'publisher', 'author']
    list_editable = ['price', 'stock', 'availible']
    list_per_page = 20

admin.site.register(Book, BookAdmin)