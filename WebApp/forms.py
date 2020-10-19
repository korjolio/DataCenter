from django import forms
from django.forms import ModelForm
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pedido

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2' ]

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['tipo_plan', 'vigencia', 'dominio', 'cert_ssl', 'nombre', 'a_paterno' , 'a_materno', 'rut', 'email']