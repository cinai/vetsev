# -*- coding: utf-8 -*-
from django.db import models
from clinica.models import Mascota 
from django.utils import timezone

ESTADO_PAGO_CHOICES = (
    ('Pendiente','Pendiente'),
    ('Parcial','Parcial'),
    ('Pagado','Pagado'),
)

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
    monto = models.IntegerField(default=0,blank=True) #corresponde a la suma de todos los ingresos menos los egresos
    saldo = models.IntegerField(default=0,blank=True) #corresponde a lo que queda para la proxima caja
    entregaDoc = models.IntegerField(default=0,blank=True) #corresponde a lo que se retira en efectivo
    tipo_turno = models.CharField(max_length=6,choices=TIPO_TURNO_CHOICES)
    fechaCreacion = models.DateTimeField()
    fechaCierre = models.DateTimeField(null=True,blank=True)
    revisado = models.BooleanField(blank=True,default=False) #corresponde si fue revisado por los admin

    def __str__(self):
        return self.tipo_turno+ " N°: "+ str(self.id)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=14)
    telefono2 = models.CharField(max_length=14,blank=True,null=True)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=40,default="Temuco")
    mail = models.EmailField(max_length=254,blank=True,null=True)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.fecha_ingreso = timezone.now()
        return super(Cliente, self).save(*args, **kwargs)

    def obtener_mascotas(self):
        mascotas = Mascota.objects.filter(cliente=self.pk)
        return mascotas

    def suscrito(self):
        n_mascotas = Mascota.objects.filter(cliente=self.pk).count()
        n_mascotas_suscritas = Mascota.objects.filter(cliente=self.pk,suscrito=True).count()
        if n_mascotas == n_mascotas_suscritas:
            return True
        return False

# Tipo_Pago es solo chars, la idea es hacer un formulario para cada uno
# bassado en un modelo
class Ingreso(models.Model):
    TIPO_PAGO_CHOICES =(
        ('Efectivo', 'Efectivo'),
        ('RedCompra', 'RedCompra'),
        ('Cheque', 'Cheque'),
    )
    descripcion = models.CharField(max_length=200,blank=True,null=True)
    fecha = models.DateTimeField()
    n_boleta = models.IntegerField(default=0,blank=True,null=True)
    tipo_pago =models.CharField(max_length=15,choices=TIPO_PAGO_CHOICES,default='Efectivo',null=True)
    n_cheque = models.IntegerField(default=0,blank=True, null=True)
    caja = models.ForeignKey(Caja)
    cliente = models.ForeignKey('Cliente',null=True,blank=True)
    estado = models.CharField(max_length=20,choices=ESTADO_PAGO_CHOICES,default='Pendiente',null=True)

    def __str__(self):
        return "Ingreso "+str(self.pk)

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

    def __str__(self):
        return self.nombre


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
