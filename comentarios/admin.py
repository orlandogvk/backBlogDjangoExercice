from django.contrib import admin
from comentarios.models import Comentario

# Register your models here.



class ComentariosAdmin(admin.ModelAdmin):
    list_display = ("descripcion",)
    search_fields = ("descripcion",)


admin.site.register(Comentario, ComentariosAdmin)


