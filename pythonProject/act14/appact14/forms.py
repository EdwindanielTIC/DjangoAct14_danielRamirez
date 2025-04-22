from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class logginForm(forms.ModelForm):
    class Meta:
        fields = ['email','password']
        model = Usuario


class createUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombre', 'apellido', 'password']