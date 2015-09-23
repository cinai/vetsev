# -*- coding: utf-8 -*-
from django.db import models


class Item_Productos(models.Model):
    TIPO_ITEM_CHOICES = (
        ('Farmacos', 'Fármacos'),
        ('Alimentos', 'Alimentos'),
        ('Productos', 'Productos Mascotería'),
        ('Insumos', 'Insumos'),
        ('Otros','Otros')
    )
    tipo = models.CharField(max_length=20,choices=TIPO_ITEM_CHOICES)
    descripcion = models.CharField(max_length=100)
    valor_venta = models.IntegerField(default=0)


class Inventario_Producto(models.Model):
    item = models.ForeignKey(Item_Productos)
    cantidad = models.IntegerField(default=1)
    ultima_mod = models.DateTimeField()


class Item_Inmueble(models.Model):
    descripcion = models.CharField(max_length=200)
    costo = models.IntegerField(default=0)


class Inventario_Inmueble(models.Model):
    item = models.ForeignKey(Item_Inmueble)
    cantidad = models.IntegerField(default=1)
    ultima_mod = models.DateTimeField()


class Caja(models.Model):
    TIPO_TURNO_CHOICES = (
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
    )
    monto = models.IntegerField(default=0)
    saldo = models.IntegerField(default=0)
    entregaDoc = models.IntegerField(default=0,blank=True)
    tipo_turno = models.CharField(max_length=6,choices=TIPO_TURNO_CHOICES)
    fechaCreacion = models.DateTimeField()
    fechaCierre = models.DateTimeField()
    revisado = models.BooleanField(blank=True,default=False)


class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=14)
    direccion = models.CharField(max_length=100)


# Tipo_Pago es solo chars, la idea es hacer un formulario para cada uno
# bassado en un modelo
class Ingreso(models.Model):
    TIPO_PAGO_CHOICES =(
        ('Efectivo', 'Efectivo'),
        ('RedCompra', 'RedCompra'),
        ('Cheque', 'Cheque'),
    )
    descripcion = models.CharField(max_length=200)
    cantidad = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    n_boleta = models.IntegerField(default=0)
    tipo_pago =models.CharField(max_length=15,choices=TIPO_PAGO_CHOICES)
    n_cheque = models.IntegerField(default=0,blank=True)
    caja = models.ForeignKey(Caja)
    cliente = models.ForeignKey(Cliente)


class Observacion(models.Model):
    Descripcion = models.CharField(max_length=300)
    fecha = models.DateTimeField()
    caja = models.ForeignKey(Caja)


class Trabajador(models.Model):
    LABOR_CHOICES =(
        ('Peluquera', 'Peluquera'),
        ('Secretaria', 'Secretaria'),
        ('Veterinaro', 'Veterinario'),
        ('Auxiliar', 'Auxiliar'),
    )
    nombre = models.CharField(max_length=50)
    labor = models.CharField(max_length=20,choices=LABOR_CHOICES)
    rut = models.CharField(max_length=12,primary_key=True)
    telefono = models.CharField(max_length=12)
    sueldo = models.IntegerField(default=0,blank=True)


class Horario(models.Model):
    dia = models.CharField(max_length=10)
    hora_inicio = models.IntegerField()
    hora_salida = models.IntegerField()
    trabajador = models.ForeignKey(Trabajador)


class Pago_Sueldos(models.Model):
    descripcion = models.CharField(max_length=100)
    trabajador = models.ForeignKey(Trabajador)
    monto = models.IntegerField(default=0)
    fecha = models.DateTimeField()


class Venta(models.Model):
    cantidad = models.IntegerField(default=1)
    item = models.ForeignKey(Item_Productos)
    ingreso = models.ForeignKey(Ingreso)


class Compra_A_Proveedor(models.Model):
    item = models.ForeignKey(Item_Productos)
    cantidad = models.IntegerField(default=1)
    costo = models.IntegerField(default=0)
    fecha = models.DateTimeField()


class Egreso_Productos(models.Model):
    item = models.ForeignKey(Item_Productos)
    motivo = models.CharField(max_length=100)
    fecha = models.DateTimeField()


class Pago_Cuentas(models.Model):
    TIPO_CUENTA_CHOICES= (
        ('Agua', 'Agua'),
        ('Arriendo', 'Arriendo'),
        ('Gas', 'Gas'),
        ('Internet', 'Internet'),
        ('Luz', 'Luz'),
        ('Telefono', 'Teléfono'),
        ('Otro', 'Otro'),
    )
    tipo = models.CharField(max_length=12,choices=TIPO_CUENTA_CHOICES)
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    monto = models.IntegerField(default=0)
    fecha_ingreso = models.DateTimeField()
    fecha_pago = models.DateTimeField(blank=True,null=True)
    pagada = models.BooleanField(default=False,blank=True)


class Compra_Inmueble(models.Model):
    item = models.ForeignKey(Item_Inmueble)
    cantidad = models.IntegerField()
    costo = models.IntegerField()
    fecha = models.DateTimeField()
