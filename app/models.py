from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publicacion (models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User , on_delete=models.CASCADE) #Si un usuario se elimina, todas las publicaciones de dicho usuario se eliminaran tambien.

    def __str__(self) -> str:
        return f"{self.titulo} de {self.autor}"