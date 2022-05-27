from django import forms

from blog.models import Blog, Tag
# from .models import Tag

class BlogForm(forms.ModelForm):
    class Meta:
        """ Cоздаем инпуты """

        model = Blog
        fields = ["title", "description", "tag"]

        widgets = {
            "title" : forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title",
            }),

            "description": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Description",
            }),

            "tag" : forms.Select(attrs={
                "class": "form-control",
            })
        }

        labels = {
            "title" : "",
            "description" : "",
        }

    def cleaned(self):
        """ Очищаем форму и проверяем на ошибки """
        
        title = self.cleaned_data["title"].lower()
        description = self.cleaned_data["description"]

        if title == "Запрещенное слово":
            raise forms.ValidationError("Запрещенное слово")
        
        return {
            "title": title,
            "description": description,
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["tag"]
        
        widgets = {
            "tag": forms.TextInput(attrs={
                "class": "form-control"
            })
        }
        

# initial = "undefined" - С помощью параметра initial можно установить значения по умолчанию.
# Параметр help_text устанавливает подсказку рядом с полем ввода:
# Выключить валидацию required=False
