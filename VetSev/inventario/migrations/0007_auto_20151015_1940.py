# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_auto_20151015_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='fechaCierre',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
