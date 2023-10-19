# keeping a url file in the individual application folder can make it easier to use later on and keep it neater overall

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'), # blog home page
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail') # this one is suppose to show specific blog post details
]

# slug is just a fancy way of saying it is user friendly and URL friendly, it is short for a slug string
