from django.urls import path
from . import views


app_name='blog'



urlpatterns = [
    path('', views.blogView, name='blog_list'),
    path('<int:id>/detail/', views.blogDetail, name='blog_detail'),
    path('add-blog/', views.addBlog, name="add_blog")
]