from django import forms
from .models import Usuario

class logginForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Usuario


class createUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombre', 'apellido', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }