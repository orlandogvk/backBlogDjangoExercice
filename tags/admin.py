from django.contrib import admin
from tags.models import Tag

# Register your models here.


class TagsAdmin(admin.ModelAdmin):
    list_display = ("descripcion",)
    search_fields = ("descripcion",)


admin.site.register(Tag, TagsAdmin)


