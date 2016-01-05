# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20150923_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='comuna',
            field=models.CharField(default='Temuco', max_length=40),
        ),
        migrations.AddField(
            model_name='cliente',
            name='mail',
            field=models.EmailField(blank=True, null=True, max_length=254),
        ),
        migrations.AddField(
            model_name='cliente',
            name='suscrito',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono2',
            field=models.CharField(blank=True, null=True, max_length=14),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Parcial', 'Parcial'), ('Pagado', 'Pagado')], default='Efectivo', max_length=20),
        ),
    ]
