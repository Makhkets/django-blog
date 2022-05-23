
from django.urls import path

from .views import *

urlpatterns = [
    path('', blog, name="blog_url"),
    path('add', add_page, name="add_page_url"),
    path('<str:id>', blog_open, name='blog_open_url'),
]