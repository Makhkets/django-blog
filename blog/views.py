from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import Register

from loguru import logger

# Create your views here.
def blog(request):
    blog = Blog.objects.all()

    return render(request=request,
     template_name="blog/index.html", context={"cards" : blog})

def blog_open(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/page.html", context={
        "title" : blog.title,
        "description" : blog.description
    })

def add_page(request):
    
    if request.method == "POST":
        if Register(request.POST).is_valid():
            
            title = request.POST.get('title')
            description = request.POST.get('description')

            Blog.objects.create(title=title, description=description)
            return redirect(reverse("blog_url"))

        else: return HttpResponse("error")

    return render(request, "blog/add.html", context={"form" : Register()})


