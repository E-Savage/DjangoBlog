from django.contrib import admin
from .models import Post

# Register your models here
# registration is so that it becomes viewable from the admin side of the website

admin.site.register(Post)