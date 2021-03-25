from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog


# Create your views here.

def blogView(request):
    blogs = Blog.objects.all()
    hiu = "asdfsdf"


 
    return render(request, 'blog/blog_list.html', {'blogs':blogs,'hiu':hiu})

