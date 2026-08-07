from django.forms import ModelForm, TextInput, Textarea

from .models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Описание фильма',
            }),
            'review': Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Ваш отзыв',
            }),
        }
