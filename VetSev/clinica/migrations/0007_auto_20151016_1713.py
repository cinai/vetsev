# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_auto_20151016_1302'),
        ('clinica', '0006_auto_20151016_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago_Cuotas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
                ('mascota', models.ForeignKey(to='clinica.Mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Pago_Suscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
                ('mascota', models.ForeignKey(to='clinica.Mascota')),
            ],
        ),
        migrations.RemoveField(
            model_name='cuotas',
            name='ingreso',
        ),
        migrations.RemoveField(
            model_name='suscripcion',
            name='ingreso',
        ),
        migrations.DeleteModel(
            name='Cuotas',
        ),
        migrations.DeleteModel(
            name='Suscripcion',
        ),
    ]
