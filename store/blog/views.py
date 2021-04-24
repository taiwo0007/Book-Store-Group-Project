from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from shop.models import Review, Book
from .forms import BlogForm
from PIL import Image, ImageOps
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

@login_required()
def addBlog(request):
    try: 
        books = Book.objects.get(id=request.POST['book_blog'])
        obj = Blog.objects.create(
            title = request.POST['title'],
            author= request.user,
            body = request.POST['body'],
            image = request.FILES['image'],
            book_blog = books

        )
        obj.save()
        messages.success(request, " Blog has been created ")
        return redirect('/accounts/profile/')
    
    except Exception as e:
        messages.alert(request, " Blog has not been created ")
        return redirect('/accounts/profile/')

    """
    if request.method == 'POST':
        form = BlogForm(title = 'kbkb')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
        """



def blogView(request):
    blogs = Blog.objects.all()
    hiu = "asdfsdf"
    print(blogs[0].id)


 
    return render(request, 'blog/blog_list.html', {'blogs':blogs,'hiu':hiu})


def blogDetail(request, id):
    blogs = get_object_or_404(Blog, id=id)
    author = get_object_or_404(Blog, id=id)
    books = Book.objects.get(id=author.book_blog.id)
    
    
    reviews = Review.objects.filter(name=author.author)[:5]
    
    
   
    #reviewss = Review.objects.filter(name=)
   
  

    #authors = Blog.objects.get(author = request.user)
    #reviews = Review.objects.filter()
    

    #reviewd = Review.objects.all().filter(user=request.user)
    #print(author)

    
    return render(request, 'blog/blog_detail.html',{'reviews':reviews, 'blogs':blogs, 'books':books})
