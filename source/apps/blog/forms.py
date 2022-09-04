from dataclasses import fields
#from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import post

class CreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:"" for k in fields}

class FormPost(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'text', 'imagen')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'first_name')

