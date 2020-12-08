from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer
from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer
from tags.models import Tag
from tags.serializers import TagSerializer


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination


    @action(methods=['GET','POST','DELETE'], detail=True)
    def tags(self, request, pk=None):
        publica = self.get_object()
        if request.method == 'GET':
            serializer = TagSerializer(publica.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == 'POST':
            tags_id = request.data['tags_ids']
            print(tags_id)
            for tag_id in tags_id:
                tag = Tag.objects.get(id=int(tag_id))
                publica.tags.add(tag)

            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            tags_id = request.data['tags_ids']
            print(tags_id)
            for tag_id in tags_id:
                tag = Tag.objects.get(id=int(tag_id))
                publica.tags.remove(tag)

            return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def comentarios(self, request, pk=None):
        publica = self.get_object()
        # print(publica)
        comment = Comentario.objects.filter(publicacion=publica)
        # print(comment)
        if request.method == 'GET':
            serializer = ComentarioSerializer(comment, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)


