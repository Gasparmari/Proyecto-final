from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dataclasses import fields



class BandaForm(forms.Form):
    name = forms.CharField(max_length=20)
    origen = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=1000)
    anio_creacion = forms.CharField(max_length=20)
    integrantes = forms.CharField(max_length=20)


class  UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label= 'Contrasenia', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contrasenia', widget= forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_text= {k:"" for k in fields }
