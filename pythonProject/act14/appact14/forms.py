from django import forms
from .models import Usuario


class logginForm(forms.ModelForm):
    class Meta:
        fields = ['email','password']
        model = Usuario


class createUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','nombre', 'apellido', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }