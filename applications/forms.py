from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Tu modelo personalizado

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'email', 'password1', 'password2']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo electrónico',
        }