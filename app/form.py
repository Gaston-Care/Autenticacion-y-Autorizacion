from django import forms #llamo a la biblioteca de django el formulario que ofrece para la creacion de usuario
from django.contrib.auth.models import User #llamo al modelo que cree de usuario
from django.contrib.auth.forms import UserCreationForm #lo modifico a mi gusto al formulario de registro

class RegistroFormulario(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']