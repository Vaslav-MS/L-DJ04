from .models import News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'autor', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Содержание новости'}),
            'autor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Дата публикации'}),
        }