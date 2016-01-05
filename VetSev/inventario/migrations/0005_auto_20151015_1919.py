# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_cliente_fecha_ingreso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='suscrito',
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Parcial', 'Parcial'), ('Pagado', 'Pagado')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='tipo_pago',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('RedCompra', 'RedCompra'), ('Cheque', 'Cheque')], default='Efectivo', max_length=15),
        ),
    ]
