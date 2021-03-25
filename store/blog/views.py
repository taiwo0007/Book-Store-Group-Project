from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog
from shop.models import Review, Book


# Create your views here.

def blogView(request):
    blogs = Blog.objects.all()
    hiu = "asdfsdf"
    print(blogs[0].id)


 
    return render(request, 'blog/blog_list.html', {'blogs':blogs,'hiu':hiu})


def blogDetail(request, id):
    blogs = get_object_or_404(Blog, id=id)
    author = get_object_or_404(Blog, id=id)
    books = Book.objects.get(id=author.book_blog.id)
    
    
    reviews = Review.objects.filter(name=author.author)
    
    
   
    #reviewss = Review.objects.filter(name=)
   
  

    #authors = Blog.objects.get(author = request.user)
    #reviews = Review.objects.filter()
    

    #reviewd = Review.objects.all().filter(user=request.user)
    #print(author)

    
    return render(request, 'blog/blog_detail.html',{'reviews':reviews, 'blogs':blogs, 'books':books})
