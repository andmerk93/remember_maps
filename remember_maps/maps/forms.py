from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Post

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('point', 'text',)
        labels = {
            'point': 'Место на карте',
            'text': 'Текст записи',
        }
        help_texts = {
            'text': 'Поделись впечатлением',
            'point': 'Поставь точку на карте',
        }


class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
