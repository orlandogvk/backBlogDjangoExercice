from rest_framework import serializers
from publicaciones.models import Publicacion


class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ('id', 'titulo', 'descripcion', 'fecha', 'autor', 'tags')

