from django.shortcuts import reverse
from django.db import models


# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField(null=False)
    tag = models.ForeignKey("Tag", on_delete=models.PROTECT, blank=True)
    date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog_open_url', kwargs={"id": self.id})

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    tag = models.CharField(unique=True, max_length=15)

    # def get_absoulute_url(self):
    #     return reverse("tag_open_url", kwargs={"id" : self.id})

    def __str__(self) -> str:
        return self.tag