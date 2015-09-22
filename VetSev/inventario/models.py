from django.db import models

# Create your models here.
class Ingreso(models.Model):
    descripcion = models.CharField(max_length=200)
    cantidad = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    n_boleta = models.IntegerField(default=0)
    tipo_pago =models.ForeignKey(Tipo_Pago)
    n_cheque = models.IntegerField(default=0)
    caja = models.ForeignKey(Caja)
    cliente = models.ForeignKey(Cliente)

#Tipo_Pago es solo chars, la idea es hacer un formulario para cada uno
#bassado en un modelo
class Tipo_Pago(models.Model):
    tipo = models.CharField(max_length=200)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=14)
    direccion = models.CharField(max_length=100)

class Caja(models.Model):
    monto = models.IntegerField(default=0)
    saldo = models.IntegerField(default=0)
    entregaDoc = models.IntegerField(default=0)
    tipo_turno = models.ForeignKey(Tipo_Turno)
    fechaCreacion = models.DateTimeField()
    fechaCierre = models.DateTimeField()

class Tipo_Turno(models.Model):
    tipo = models.CharField(max_length=30,required=True,primary_key=True)

class Observacion(models.Model):
    Descripcion = models.CharField(max_length=300)
    fecha = models.DateTimeField()
    caja = models.ForeignKey(Caja)

class Venta(models.Model):
    cantidad = models.IntegerField(default=1)
    item = models.ForeignKey(Item)
    ingreso = models.ForeignKey(Ingreso)

class Trabajador(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12,primary_key=True)
    telefono = models.CharField(max_length=12)

class Cargo(models.Model):
    nombre = models.CharField(max_length=10, default="Veterinario")

class Horario(models.Model):
    dia = models.CharField()
    hora_inicio = models.IntegerField()
    hora_salida = models.IntegerField()
    trabajador = models.ForeignKey(Trabajador)

