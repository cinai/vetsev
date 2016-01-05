# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='sueldo',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='labor',
            field=models.CharField(choices=[('Peluquera', 'Peluquera'), ('Secretaria', 'Secretaria'), ('Veterinaro', 'Veterinario'), ('Auxiliar', 'Auxiliar')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Labor',
        ),
    ]
