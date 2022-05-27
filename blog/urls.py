
from django.urls import path

from .views import *

urlpatterns = [
    path('', blog, name="blog_url"),
    path('add_article', Add_blog.as_view(), name="add_page_url"),
    path('add_tag', add_page, name="add_page_tag"),
    path('<str:id>', blog_open, name='blog_open_url'),
]