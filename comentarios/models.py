from django.db import models
from publicaciones.models import Publicacion



class Comentario(models.Model):
    descripcion=models.CharField(max_length=200)
    publicacion= models.ForeignKey(Publicacion, on_delete=models.CASCADE,
                                   null=False, blank=False, related_name='comentarios')
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.descripcion
