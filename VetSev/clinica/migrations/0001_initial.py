# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20151007_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cirugia',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
                ('veterinario', models.ForeignKey(to='inventario.Trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('monto', models.IntegerField(default=7500)),
                ('fecha_ingreso', models.DateTimeField()),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
            ],
        ),
        migrations.CreateModel(
            name='Cuotas',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
            ],
        ),
        migrations.CreateModel(
            name='Evento_Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('estado', models.CharField(choices=[('Sin Avisar', 'Sin Avisar'), ('Avisado', 'Avisado'), ('Confirmado', 'Confirmado'), ('En curso', 'En curso'), ('Finalizado', 'Finalizado')], max_length=30)),
                ('tipo', models.CharField(choices=[('Baño', 'Baño'), ('Peluqueria', 'Peluquería'), ('Antiparasitario', 'Antiparasitario'), ('Vacuna', 'Vacuna'), ('Consulta', 'Consulta'), ('Hospitalizacion', 'Hospitalización'), ('Control', 'Control')], max_length=20)),
                ('descripcion', models.CharField(max_length=40)),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_evento', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ficha_Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('anamnesis', models.TextField(max_length=400)),
                ('peso', models.PositiveIntegerField()),
                ('temperatura', models.PositiveIntegerField()),
                ('mucosas', models.CharField(max_length=30)),
                ('piel', models.CharField(max_length=30)),
                ('torax', models.CharField(max_length=30)),
                ('abdomen', models.CharField(max_length=30)),
                ('observaciones', models.TextField(max_length=400)),
                ('diagnostico', models.TextField(max_length=400)),
                ('tratamiento', models.TextField(max_length=400)),
                ('consulta', models.ForeignKey(to='clinica.Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Ficha_Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospitalizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('diagnostico', models.CharField(max_length=150)),
                ('estado', models.CharField(choices=[('Reservado', 'Reservado'), ('Alojado', 'Alojado'), ('Retirado', 'Retirado'), ('Fallecido', 'Fallecido')], max_length=30)),
                ('estado_pago', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Parcial', 'Parcial'), ('Pagado', 'Pagado')], max_length=14)),
                ('fecha_ingreso', models.DateTimeField(blank=True)),
                ('fecha_retiro', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('estado', models.CharField(choices=[('Reservado', 'Reservado'), ('Alojado', 'Alojado'), ('Retirado', 'Retirado')], max_length=30)),
                ('fecha_ingreso', models.DateTimeField(blank=True)),
                ('fecha_retiro', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('especie', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('sexo', models.CharField(choices=[('Hembra', 'Hembra'), ('Macho', 'Macho')], max_length=20)),
                ('cliente', models.ForeignKey(to='inventario.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Observaciones_Generales',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('observacion', models.TextField(max_length=300)),
                ('mascota', models.ForeignKey(to='clinica.Mascota')),
                ('trabajador', models.ForeignKey(to='inventario.Trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Pago_Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
                ('veterinario', models.ForeignKey(to='inventario.Trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Pago_Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('dias', models.IntegerField(default=1)),
                ('hotel', models.ForeignKey(to='clinica.Hotel')),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
            ],
        ),
        migrations.CreateModel(
            name='Pago_Peluqueria',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
                ('trabajador', models.ForeignKey(to='inventario.Trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Peluqueria',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('estado', models.CharField(choices=[('Ingresado', 'Ingresado'), ('Listo para retirar', 'Listo'), ('Retirado', 'Retirado')], max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateTimeField(blank=True)),
                ('fecha_retiro', models.DateTimeField(blank=True)),
                ('mascota', models.ForeignKey(to='clinica.Mascota')),
                ('peluquera', models.ForeignKey(to='inventario.Trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
                ('veterinario', models.ForeignKey(to='inventario.Trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='mascota',
            field=models.ForeignKey(to='clinica.Mascota'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='trabajador',
            field=models.ForeignKey(to='inventario.Trabajador'),
        ),
        migrations.AddField(
            model_name='hospitalizacion',
            name='mascota',
            field=models.ForeignKey(to='clinica.Mascota'),
        ),
        migrations.AddField(
            model_name='hospitalizacion',
            name='trabajador',
            field=models.ForeignKey(to='inventario.Trabajador'),
        ),
        migrations.AddField(
            model_name='ficha_hospital',
            name='mascota',
            field=models.ForeignKey(to='clinica.Mascota'),
        ),
        migrations.AddField(
            model_name='ficha_hospital',
            name='trabajador',
            field=models.ForeignKey(to='inventario.Trabajador'),
        ),
        migrations.AddField(
            model_name='evento_mascota',
            name='mascota',
            field=models.ForeignKey(to='clinica.Mascota'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='mascota',
            field=models.ForeignKey(to='clinica.Mascota'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='veterinario',
            field=models.ForeignKey(to='inventario.Trabajador'),
        ),
    ]
