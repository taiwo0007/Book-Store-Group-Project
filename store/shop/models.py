from django.db import models
import uuid
from django.urls import reverse

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        editable = False)

    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    popularity = models.PositiveSmallIntegerField()
    books = models.ManyToManyField('Books')

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_aboslute_url(self):
        return reverse('shop:books_by_category', args=[self.id])

    def _str_(self):
        return self.name

class Author(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable =False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.PositiveSmallIntegerField()
    about = models.TextField(blank=True)

class Books(models.Model):
        id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
        iban = models.CharField(unique=True, max_length=250)
        title = models.CharField(max_length=250, unique=True)
        synopsis = models.TextField(blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        star_rating = models.PositiveSmallIntegerField()
        image = models.ImageField(upload_to='books', blank=True)
        stock = models.IntegerField()
        availible = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        updated = models.DateTimeField(auto_now=True, blank=True, null=True)
        pub_date = models.DateField(blank=True, null=True)
        num_pages = models.IntegerField()
        publisher = models.CharField(max_length=250)
        author = models.ForeignKey(Author, related_name='authors', on_delete=models.CASCADE)

        class Meta:
            ordering = ('title', )
            verbose_name = 'book'
            verbose_name_plural = 'books'

        def get_absolute_url(self):
            return reverse('shop:book_detail', args=[self.category.id, self.id])
        
        def __str__(self):
            return self.title