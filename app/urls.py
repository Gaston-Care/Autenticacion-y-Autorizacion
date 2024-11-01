from django.urls import path
from app.views import CrearPublicacion, DetallePublicacion, EditarPublicacion, EliminarPublicacion, Publicaciones, home_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home_view, name='home'),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('publicaciones/',Publicaciones.as_view(), name='publicaciones'),
    path('publicaciones/crear', CrearPublicacion.as_view(), name='publicaciones_crear'),
    path('publicaciones/detalle/<int:pk>/', DetallePublicacion.as_view(), name='detalle_publicacion'),
    path('publicaciones/editar/<int:pk>/', EditarPublicacion.as_view(), name='editar_publicacion'),
    path('publicaciones/eliminar/<int:pk>/', EliminarPublicacion.as_view(), name='eliminar_publicacion'),
]