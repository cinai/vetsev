# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_auto_20151015_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingreso',
            name='cantidad',
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='descripcion',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='estado',
            field=models.CharField(max_length=20, null=True, default='Pendiente', choices=[('Pendiente', 'Pendiente'), ('Parcial', 'Parcial'), ('Pagado', 'Pagado')]),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='n_boleta',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='n_cheque',
            field=models.IntegerField(blank=True, null=True, default=0),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='tipo_pago',
            field=models.CharField(max_length=15, null=True, default='Efectivo', choices=[('Efectivo', 'Efectivo'), ('RedCompra', 'RedCompra'), ('Cheque', 'Cheque')]),
        ),
    ]
