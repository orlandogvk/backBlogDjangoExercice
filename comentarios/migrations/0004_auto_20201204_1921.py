# Generated by Django 2.2.14 on 2020-12-05 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_auto_20201204_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='publicaciones.Publicacion'),
        ),
    ]