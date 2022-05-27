from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from . import utils
from . import models
from . import forms

from loguru import logger

# Create your views here.
def blog(request):
    blog = models.Blog.objects.all()
    return render(request=request, template_name="blog/index.html", context={"cards" : blog})

def blog_open(request, id):
    blog = models.Blog.objects.get(id=id)
    return render(request, "blog/page.html", context={"blog": blog})

def add_page(request):
    if request.method == "POST":
        f = forms.BlogForm(request.POST)
        if f.is_valid():
            f.save()

            return redirect(reverse("blog_url"))

    return render(request, "blog/add.html", context={"form" : forms.BlogForm()})


class Add_blog(utils.ObjectAddMixin, View):
    form = forms.BlogForm
    template = "blog/add.html"
    reverse_name = "blog_open_url"

class Add_tag(utils.ObjectAddMixin, View):
    pass
