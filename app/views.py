from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from app.forms import RegistroFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
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
    fields = ['titulo','contenido']
    template_name = 'crear_publicacion.html'
    success_url = reverse_lazy('publicaciones')
    permission_required = "app.addPublicacion" # Permiso para agregar una publicacion

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class Publicaciones(LoginRequiredMixin, ListView):
    model = Publicacion
    paginate_by=4
    template_name = 'publicaciones.html'
    context_object_name = 'publicaciones'
    permission_required = "app.viewPublicacion"

class DetallePublicacion(DetailView):
    model = Publicacion
    template_name = 'detalle_publicacion.html'

class EditarPublicacion(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Publicacion
    fields = ['titulo', 'contenido']
    template_name = 'editar_publicacion.html' # Template no creado todavia no probar!!!!!
    success_url = reverse_lazy('publicaciones')
    permission_required = "app.changePublicacion" # Permiso para cambiar una publicacion

    def get_queryset(self):
        return Publicacion.objects.filter(autor=self.request.user)
    
class EliminarPublicacion(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        publicacion = get_object_or_404(Publicacion, pk=pk, autor=request.user)
        publicacion.delete()
        return redirect('publicaciones')  # Redirige a la lista de publicaciones después de eliminar

    def get(self, request, pk, *args, **kwargs):
        publicacion = get_object_or_404(Publicacion, pk=pk, autor=request.user)
        # Puedes mostrar un mensaje o simplemente redirigir a otra vista
        return redirect('publicaciones')  # O renderizar una respuesta que informe que no se puede acceder a esta vista