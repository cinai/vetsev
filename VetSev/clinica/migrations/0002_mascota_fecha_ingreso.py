# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 10, 8, 1, 42, 2, 663503, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
