# Generated by Django 2.2.14 on 2020-12-04 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_auto_20201204_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='publicaciones',
            new_name='publicacion',
        ),
    ]