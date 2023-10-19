from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from .models import Post

# Create your views here.

'''
    new view called post_list
'''

def post_list(request):
    posts = admin.site.site_header(Post.objects.all())
    return render(request, 'admin/blog/post_list.html', {'posts': posts})

urlpatterns = [
    path('post_list/', post_list),
]
