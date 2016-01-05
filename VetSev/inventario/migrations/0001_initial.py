# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField(default=0)),
                ('saldo', models.IntegerField(default=0)),
                ('entregaDoc', models.IntegerField(blank=True, default=0)),
                ('tipo_turno', models.CharField(max_length=6, choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde')])),
                ('fechaCreacion', models.DateTimeField()),
                ('fechaCierre', models.DateTimeField()),
                ('revisado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('rut', models.CharField(max_length=12)),
                ('telefono', models.CharField(max_length=14)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Compra_A_Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('costo', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra_Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('costo', models.IntegerField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Egreso_Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=10)),
                ('hora_inicio', models.IntegerField()),
                ('hora_salida', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
                ('n_boleta', models.IntegerField(default=0)),
                ('tipo_pago', models.CharField(max_length=15, choices=[('Efectivo', 'Efectivo'), ('RedCompra', 'RedCompra'), ('Cheque', 'Cheque')])),
                ('n_cheque', models.IntegerField(blank=True, default=0)),
                ('caja', models.ForeignKey(to='inventario.Caja')),
                ('cliente', models.ForeignKey(to='inventario.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario_Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('ultima_mod', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('ultima_mod', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Item_Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('costo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20, choices=[('Farmacos', 'Fármacos'), ('Alimentos', 'Alimentos'), ('Productos', 'Productos Mascotería'), ('Insumos', 'Insumos'), ('Otros', 'Otros')])),
                ('descripcion', models.CharField(max_length=100)),
                ('valor_venta', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=300)),
                ('fecha', models.DateTimeField()),
                ('caja', models.ForeignKey(to='inventario.Caja')),
            ],
        ),
        migrations.CreateModel(
            name='Pago_Cuentas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=12, choices=[('Agua', 'Agua'), ('Arriendo', 'Arriendo'), ('Gas', 'Gas'), ('Internet', 'Internet'), ('Luz', 'Luz'), ('Telefono', 'Teléfono'), ('Otro', 'Otro')])),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('monto', models.IntegerField(default=0)),
                ('fecha_ingreso', models.DateTimeField()),
                ('fecha_pago', models.DateTimeField(blank=True, null=True)),
                ('pagada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pago_Sueldos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('monto', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('rut', models.CharField(primary_key=True, max_length=12, serialize=False)),
                ('telefono', models.CharField(max_length=12)),
                ('labor', models.ForeignKey(to='inventario.Labor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('ingreso', models.ForeignKey(to='inventario.Ingreso')),
                ('item', models.ForeignKey(to='inventario.Item_Productos')),
            ],
        ),
        migrations.AddField(
            model_name='pago_sueldos',
            name='trabajador',
            field=models.ForeignKey(to='inventario.Trabajador'),
        ),
        migrations.AddField(
            model_name='inventario_producto',
            name='item',
            field=models.ForeignKey(to='inventario.Item_Productos'),
        ),
        migrations.AddField(
            model_name='inventario_inmueble',
            name='item',
            field=models.ForeignKey(to='inventario.Item_Inmueble'),
        ),
        migrations.AddField(
            model_name='horario',
            name='trabajador',
            field=models.ForeignKey(to='inventario.Trabajador'),
        ),
        migrations.AddField(
            model_name='egreso_productos',
            name='item',
            field=models.ForeignKey(to='inventario.Item_Productos'),
        ),
        migrations.AddField(
            model_name='compra_inmueble',
            name='item',
            field=models.ForeignKey(to='inventario.Item_Inmueble'),
        ),
        migrations.AddField(
            model_name='compra_a_proveedor',
            name='item',
            field=models.ForeignKey(to='inventario.Item_Productos'),
        ),
    ]
