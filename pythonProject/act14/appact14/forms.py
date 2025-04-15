from django import forms
from .models import Usuario

class logginForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Usuario
