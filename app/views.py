from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from app.forms import RegistroFormulario
from django.contrib.auth.decorators import login_required # Para proteger vistas.

def home_view(request):
    return render(request, 'home.html')

class RegistroUsuario(CreateView):
    template_name = 'accounts/register.html'  # Ruta a la plantilla
    form_class = RegistroFormulario  # Formulario personalizado
    success_url = reverse_lazy('login')  # Redirige despues del registro

