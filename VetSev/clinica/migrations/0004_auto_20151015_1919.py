# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0003_mascota_suscrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='especie',
            field=models.CharField(choices=[('Canino', 'Canino'), ('Felino', 'Felino'), ('Otro', 'Otro')], max_length=20),
        ),
    ]
