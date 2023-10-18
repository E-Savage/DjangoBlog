from django.db import models

# wanted to check to see if this was working

# teehee

# Create your models here.

class Post(models.Model):
    """
        This is a class to mimic a blog post that stores title, content of the blog and also the time
        that the blgo post was created at
    """

    title = models.CharField(max_length=200) # tells what control will be used for this data field 
    content = models.TextField() # shows UI control that will be used for this data field
    created_at = models.DateTimeField(auto_now_add=True) # uses date field as a UI control, automatically sets the date 
