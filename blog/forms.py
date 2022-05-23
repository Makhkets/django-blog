from django import forms

def metafield(key):
    widget = {
        "phone" : forms.TextInput(attrs={
            "class" : "phone",
            "type" : "tel",
            "placeholder" : "Телефон"
        })
    }

    return widget["key"]

class Register(forms.Form):

    title = forms.CharField()
    description = forms.CharField()


# initial = "undefined" - С помощью параметра initial можно установить значения по умолчанию.
# Параметр help_text устанавливает подсказку рядом с полем ввода:
# Выключить валидацию required=False
