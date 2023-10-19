from django.contrib import admin
from django.urls import path
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

'''
    new view called post_list
'''

# gets all the posts and displays them
def post_list(request):
    posts = admin.site.site_header(Post.objects.all())
    return render(request, 'admin/blog/post_list.html', {'posts': posts})

# gets specific post details 
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                              public_year=year, publish_month=month, publish_day=day)
    return render(request, 'blog/post_detail.html', {'post': post})

urlpatterns = [
    path('post_list/', post_list),
]
