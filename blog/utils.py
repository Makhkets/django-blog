
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse


from . import utils
from . import models
from . import forms

class ObjectAddMixin:
    form = None
    template = None
    reverse_name = None

    def get(self, request):
        return render(request=request, template_name=self.template, context={"form": self.form})
    
    def post(self, request):
        f = self.form(request.POST)
        if f.is_valid():
            response = f.save()
            return redirect(reverse(self.reverse_name, kwargs={"id": response.id}))
        
        else:
            return HttpResponse(f.errors)