from django.db import models
from tags.models import Tag

# Para acceder a la relacion
# la clase relacionada en minusculas _ set (pub1.comentario_set)
# filtros, agrupamientos, conteos

#la clase relacionada en minusculas__atributo__
class Publicacion(models.Model):

    titulo = models.CharField(max_length=200, default=None)
    descripcion = models.CharField(max_length=200, help_text="Enter field documentation")
    fecha = models.DateTimeField(null=True, blank=True)
    autor = models.CharField(max_length=100, help_text="Enter field documentation")
    tags = models.ManyToManyField(Tag, related_name='tags')
    created=models.DateTimeField(auto_now_add=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.titulo