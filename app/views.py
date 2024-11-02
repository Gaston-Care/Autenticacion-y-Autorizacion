from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from app.forms import RegistroFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from app.models import Publicacion # Para proteger vistas.

def home_view(request):
    return render(request, 'home.html')

class RegistroUsuario(CreateView):
    template_name = 'accounts/register.html'  # Ruta a la plantilla
    form_class = RegistroFormulario  # Formulario personalizado
    success_url = reverse_lazy('login')  # Redirige despues del registro

# Agregar permission_required
class CrearPublicacion(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    model = Publicacion
    permission_required = "app.add_publicacion"  # Solo los que tengan este permiso podran acceder a la vista.
    fields = ['titulo','contenido']
    template_name = 'crear_publicacion.html'
    success_url = reverse_lazy('publicaciones')
    permission_required = "app.add_publicacion"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class Publicaciones(LoginRequiredMixin, ListView):
    model = Publicacion
    paginate_by=4
    template_name = 'publicaciones.html'
    context_object_name = 'publicaciones'
    permission_required = "app.view_publicacion"

class DetallePublicacion(DetailView):
    model = Publicacion
    template_name = 'detalle_publicacion.html'

class EditarPublicacion(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Publicacion
    fields = ['titulo', 'contenido']
    template_name = 'editar_publicacion.html'
    success_url = reverse_lazy('publicaciones')
    permission_required = "app.change_publicacion"  # Solo los que tengan este permiso podran acceder a la vista.
    
    def dispatch(self, request, *args, **kwargs): # Verificacion que evita acceder a la vista EDITAR por medio de la URL
        # publicación que se va a editar
        publicacion = self.get_object()
        # Verifica si el usuario es el autor
        if publicacion.autor != request.user:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
    
class EliminarPublicacion(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Publicacion
    permission_required = "app.delete_publicacion"  # Solo los que tengan este permiso podran acceder a la vista.
    success_url = reverse_lazy('publicaciones')

    def post(self, request, *args, **kwargs):
        # Llamamos al método delete directamente
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)