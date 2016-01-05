# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20151007_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 10, 8, 1, 42, 10, 729101, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
