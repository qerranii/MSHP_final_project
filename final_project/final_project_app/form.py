from django import forms
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.

class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=100)
    password = forms.CharField(label='Password', max_length=25)