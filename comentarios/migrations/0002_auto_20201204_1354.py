# Generated by Django 2.2.14 on 2020-12-04 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='publicacion',
            new_name='publicaciones',
        ),
    ]
