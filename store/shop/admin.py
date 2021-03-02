from django.contrib import admin
from .models import Category, Book, Author


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['iban', 'title', 'price', 'star_rating', 'stock', 'availible', 'num_pages', 'publisher', 'author']
    list_editable = ['price', 'stock', 'availible']
    list_per_page = 20

admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'about']
    list_editable = ['about']
    list_per_page = 20


admin.site.register(Author, AuthorAdmin)