from django.shortcuts import reverse
from django.db import models


# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField(null=True)
    date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog_open_url', kwargs={"id": self.id})

    def __str__(self) -> str:
        return self.title

    """
представляет тип CharField - текстовое поле,
которое хранит последовательность символов. Оно
будет хранить имя человека. Для CharField обязательно 
надо указать параметр max_length, 
который задает максимальную длину хранящейся строки.
    """