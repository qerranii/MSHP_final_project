from django import forms
from django.core.validators import validate_comma_separated_integer_list
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'description']
