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

class Pago_Sueldos(models.Model):
    descripcion = models.CharField(max_length=100)
    trabajador = models.ForeignKey(Trabajador)
    monto = models.IntegerField(default=0)
    fecha = models.DateTimeField()

class Compra_A_Proveedor(models.Model):
    item = models.ForeignKey(Item_Ventas)
    cantidad = models.IntegerField(default=1)
    costo = models.IntegerField(default=0)
    fecha = models.DateTimeField()

class Egreso_Productos(models.Model):
    item = models.ForeignKey(Item_Ventas)
    motivo = models.CharField(max_length=100)
    fecha = models.DateTimeField()

class Pago_Cuentas(models.Model):
    tipo = models.ForeignKey(Tipo_Cuenta)
    descripción = models.CharField(max_length=100)
    monto = models.IntegerField(default=0)
    fecha = models.DateTimeField()

class Tipo_Cuenta(models.Model):
    tipo = models.CharField(max_length=40)

class Compra_Inmueble(models.Model):
    item = models.ForeignKey(Item_Inmueble)
    cantidad = models.IntegerField()
    costo = models.IntegerField()
    fecha = models.DateTimeField()

class Item_Ventas(models.Model):
    tipo = models.ForeignKey(Tipo_Item)
    descripcion = models.CharField(max_length=100)
    valor_venta = models.IntegerField(default=0)

class Tipo_Item(models.Model):
    tipo = models.CharField(max_length=40)

class Inventario_Producto(models.Model):
    item = models.ForeignKey(Item_Ventas)
    cantidad = models.IntegerField(default=1)
    ultima_mod = models.DateTimeField()

class Item_Inmueble(models.Model):
    descripcion = models.Charfield(max_length=200)
    costo = models.IntegerField(default=0)

class Inventario_Inmueble(models.Model):
    item = models.ForeignKey(Item_Inmueble)
    cantidad = models.IntegerField(default=1)
    ultima_mod = models.DateTimeField()

