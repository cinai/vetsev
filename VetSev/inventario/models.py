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

class Mascota(models.Model):
    cliente = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=100)

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

class Consulta(models.Model):
    monto = models.IntegerField(default=7500)
    fecha = models.DateTimeField()
    ingreso = models.ForeignKey(Ingreso)
    mascota = models.ForeignKey(Mascota)

class Venta(models.Model):
    cantidad = models.IntegerField(default=1)
    item = models.ForeignKey(Item)
    ingreso = models.ForeignKey(Ingreso)

class Pago_Hotel(models.Model):
    dias = models.IntegerField(default=1)
    hotel = models.ForeignKey(Hotel)
    ingreso = models.ForeignKey(Ingreso)

class Procedimiento(models.Model):
    descripcion = models.CharField(max_length=150)
    veterinario = models.ForeignKey(Veterinario)
    ingreso = models.ForeignKey(Ingreso)

class Pago_Peluquería(models.Model):
    ingreso = models.ForeignKey(Ingreso)
    trabajador = models.ForeignKey(Trabajador)

class Cuotas(models.Model):
    ingreso = models.ForeignKey(Ingreso)

class Suscripcion(models.Model):
    ingreso = models.ForeignKey(Ingreso)

class Pago_Hospital(models.Model):
    ingreso = models.ForeignKey(Ingreso)
    veterinario = models.ForeignKey(Trabajador)

class Cirugia(models.Model):
    ingreso = models.ForeignKey(Ingreso)
    veterinario = models.ForeignKey(Trabajador)

class Trabajador(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12,primary_key=True)
