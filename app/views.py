from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from app.forms import RegistroFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from app.models import Publicacion # Para proteger vistas.

def home_view(request):
    return render(request, 'home.html')

class RegistroUsuario(CreateView):
    template_name = 'accounts/register.html'  # Ruta a la plantilla
    form_class = RegistroFormulario  # Formulario personalizado
    success_url = reverse_lazy('login')  # Redirige despues del registro

# Agregar permission_required
class CrearPublicacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    fields = ['titulo','contenido']
    template_name = 'crear_publicacion.html'
    success_url = reverse_lazy('publicaciones')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Agregar login_required
class Publicaciones(ListView):
    model = Publicacion
    paginate_by = 4
    template_name = 'publicaciones.html'
    
    def get_queryset(self):
        return Publicacion.objects.all()