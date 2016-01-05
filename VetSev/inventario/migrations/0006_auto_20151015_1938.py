# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_auto_20151015_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='fechaCierre',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='caja',
            name='monto',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='caja',
            name='saldo',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='cliente',
            field=models.ForeignKey(to='inventario.Cliente', null=True, blank=True),
        ),
    ]
