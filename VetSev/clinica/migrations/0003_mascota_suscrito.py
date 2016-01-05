# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_mascota_fecha_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='suscrito',
            field=models.BooleanField(default=False),
        ),
    ]
