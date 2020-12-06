from django.contrib import admin
from publicaciones.models import Publicacion

# Register your models here.



class PublicacionesAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descripcion", "fecha", "autor",)
    search_fields = ("titulo",)


admin.site.register(Publicacion, PublicacionesAdmin)

