from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm): #Formulario de registro que hereda de un formulario que viene por defecto en Django: UserCreationForm
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User #Se define el modelo que está relacionado con el formulario
        fields = ['username', 'email', 'password1', 'password2'] #Definición de los campos del formulario

class AuthForm(AuthenticationForm):
    pass

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)

""" class RegisterForm(forms.Form):
    email = forms.EmailField(
        label="e-mail",
        max_length=200, 
        required=True
        )
    username = forms.CharField(
        label="Username",
        max_length=255, 
        required=True
        )
    password = forms.CharField(
        label="Password",
        min_length=8,
        widget=forms.PasswordInput(attrs=
                {"class": "form-control"}
            )
        )
    re_password = forms.CharField(
        label="Repeat password",
        min_length=8,
        widget=forms.PasswordInput(attrs=
                {"class": "form-control"}
            )
        ) """