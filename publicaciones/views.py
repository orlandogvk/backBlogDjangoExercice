from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer
from tags.models import Tag
from tags.serializers import TagSerializer


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,)


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
                tag= Tag.objects.get(id=int(tag_id))
                publica.tags.add(tag)

            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            tags_id = request.data['tags_ids']
            print(tags_id)
            for tag_id in tags_id:
                tag = Tag.objects.get(id=int(tag_id))
                publica.tags.remove(tag)

            return Response(status=status.HTTP_200_OK)
