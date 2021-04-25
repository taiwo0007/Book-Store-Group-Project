from django.db import models
import uuid
from django.urls import reverse
from django.conf import settings
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator,  MaxValueValidator


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        editable = False)

    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    popularity = models.PositiveSmallIntegerField()
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')
    '''books = models.ManyToManyField('Book')'''

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:books_by_category', args=[self.slug])

    def __str__(self):
        return self.name
 
class Author(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable =False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250,default='SOME STRING')
    age = models.PositiveSmallIntegerField()
    about = models.TextField(blank=True)

    

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Book(models.Model):
        id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
        iban = models.CharField(unique=True, max_length=250)
        title = models.CharField(max_length=250, unique=True)
        synopsis = models.TextField(blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        star_rating = models.FloatField()
        image = models.ImageField(upload_to='books', blank=True)
        stock = models.IntegerField()
        availible = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        updated = models.DateTimeField(auto_now=True, blank=True, null=True)
        pub_date = models.DateField(blank=True, null=True)
        num_pages = models.IntegerField()
        publisher = models.CharField(max_length=240)
        author = models.ForeignKey(Author, related_name='authors', on_delete=models.CASCADE)
        category = models.ForeignKey(Category, on_delete=models.CASCADE,null=False)
        slug = AutoSlugField(null=True, default=None, unique=True, populate_from='title')

        class Meta:
            ordering = ('title', )
            verbose_name = 'book'
            verbose_name_plural = 'books'
        
        def get_absolute_url(self):
            return reverse('shop:book_detail',args=[self.category.slug, self.slug])

        def temp_url(self):
            return self.category.slug, self.slug
        
        def __str__(self):
            return self.title



class WishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wished_item.title

    def get_absolute_url(self):
            return reverse('shop:wishList_books')


class Review(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=40)
    comment = models.CharField(max_length=240)
    review_item = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(default="1", validators=[MinValueValidator(1), MaxValueValidator(5)] )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject

    def get_absolute_url(self):
            return reverse('shop:book_detail',args=[self.review_item.category.slug, self.review_item.slug])



    

    

            
