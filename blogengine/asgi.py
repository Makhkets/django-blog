"""
ASGI config for blogengine project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogengine.settings')

application = get_asgi_application()


# class Course(models.Model):
#     name = models.CharField(max_length=30)
 
# class Student(models.Model):
#     name = models.CharField(max_length=30)
#     courses = models.ManyToManyField(Course)
