# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0004_auto_20151015_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
    ]
