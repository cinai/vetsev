# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0005_auto_20151015_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='ingreso',
            field=models.OneToOneField(to='inventario.Ingreso'),
        ),
    ]
