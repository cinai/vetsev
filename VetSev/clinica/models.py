# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from datetime import date

ESTADO_PAGO_CHOICES = (
    ('Pendiente','Pendiente'),
    ('Parcial','Parcial'),
    ('Pagado','Pagado'),
)


class Mascota(models.Model):
    SEXO_CHOICES = (
        ('Hembra', 'Hembra'),
        ('Macho','Macho'),
    )
    ESPECIE_CHOICES = (
        ('Canino','Canino'),
        ('Felino','Felino'),
        ('Otro','Otro'),
    )
    cliente = models.ForeignKey('inventario.Cliente')
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    especie = models.CharField(max_length=20,choices=ESPECIE_CHOICES)
    raza = models.CharField(max_length=20,null=True,blank=True)
    color = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES)
    fecha_ingreso = models.DateField()
    suscrito = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.fecha_ingreso = timezone.now()
        return super(Mascota, self).save(*args, **kwargs)

    def obtener_edad(self):
        born = self.fecha_nacimiento
        today = date.today()
        years = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        final_age = str(years) + " años"
        if years == 0:
            months = today.month - born.month - (today.day < born.day)
            final_age = str(months) + " meses"
            
        return final_age
    #TODOs
    def obtener_ultima_at(self):
        return self.fecha_ingreso


#TODO: hacer que los precios sean segun el horario y el dia
class Consulta(models.Model):
    monto = models.IntegerField(default=7500)
    fecha_ingreso = models.DateTimeField()
    ingreso = models.OneToOneField('inventario.Ingreso')
    mascota = models.ForeignKey('Mascota')
    veterinario = models.ForeignKey('inventario.Trabajador')

    def __str__(self):
        return "Consulta N°: "+str(self.id)+", "+self.mascota.nombre

#TODO: estado del pago
class Hotel(models.Model):
    ESTADO_CHOICES = (
        ('Reservado','Reservado'),
        ('Alojado','Alojado'),
        ('Retirado','Retirado'),
    )
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey('inventario.Trabajador')
    estado = models.CharField(max_length=30,choices=ESTADO_CHOICES)
    fecha_ingreso = models.DateTimeField(blank=True)
    fecha_retiro = models.DateTimeField(blank=True)


class Hospitalizacion(models.Model):
    ESTADO_CHOICES = (
        ('Reservado','Reservado'),
        ('Alojado','Alojado'),
        ('Retirado','Retirado'),
        ('Fallecido','Fallecido'),
    )
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey('inventario.Trabajador')
    diagnostico = models.CharField(max_length=150)
    estado = models.CharField(max_length=30,choices=ESTADO_CHOICES)
    estado_pago = models.CharField(max_length=14,choices=ESTADO_PAGO_CHOICES)
    fecha_ingreso = models.DateTimeField(blank=True)
    fecha_retiro = models.DateTimeField(blank=True)
    monto_diario =  models.IntegerField(default=7500)


class Pago_Hotel(models.Model):
    hotel = models.ForeignKey(Hotel)
    ingreso = models.ForeignKey('inventario.Ingreso')
    dias = models.IntegerField(default=1)


class Procedimiento(models.Model):
    descripcion = models.CharField(max_length=150)
    veterinario = models.ForeignKey('inventario.Trabajador')
    ingreso = models.ForeignKey('inventario.Ingreso')


class Pago_Peluqueria(models.Model):
    ingreso = models.ForeignKey('inventario.Ingreso')
    trabajador = models.ForeignKey('inventario.Trabajador')


class Pago_Cuotas(models.Model):
    ingreso = models.ForeignKey('inventario.Ingreso')
    mascota = models.ForeignKey('Mascota')

class Pago_Suscripcion(models.Model):
    ingreso = models.ForeignKey('inventario.Ingreso')
    mascota = models.ForeignKey('Mascota')


class Pago_Hospital(models.Model):
    ingreso = models.ForeignKey('inventario.Ingreso')
    hospitalizacion = models.ForeignKey('Hospitalizacion')

class Cirugia(models.Model):
    ingreso = models.ForeignKey('inventario.Ingreso')
    veterinario = models.ForeignKey('inventario.Trabajador')


#TODO: pensar mejor eventos y calendarios
class Evento_Mascota(models.Model):
    ESTADO_CHOICES = (
        ('Sin Avisar','Sin Avisar'),
        ('Avisado','Avisado'),
        ('Confirmado','Confirmado'),
        ('En curso','En curso'),
        ('Finalizado','Finalizado'), 
    )
    TIPO_CHOICES = (
        ('Baño','Baño'),
        ('Peluqueria','Peluquería'),
        ('Antiparasitario','Antiparasitario'),
        ('Vacuna','Vacuna'),
        ('Consulta','Consulta'),
        ('Hospitalizacion','Hospitalización'),
        ('Control','Control'),
    )
    mascota = models.ForeignKey(Mascota)
    estado = models.CharField(max_length=30,choices=ESTADO_CHOICES)
    tipo = models.CharField(max_length=20,choices=TIPO_CHOICES)
    descripcion = models.CharField(max_length=40)
    fecha_creacion = models.DateTimeField()
    fecha_evento = models.DateTimeField()


#TODO: completar ficha clinica
class Ficha_Clinica(models.Model):
    consulta = models.ForeignKey(Consulta)
    anamnesis = models.TextField(max_length=400)
    peso = models.PositiveIntegerField()
    temperatura = models.PositiveIntegerField()
    #en vola hay tipos definidos para los siguientes
    mucosas = models.CharField(max_length=30)
    piel = models.CharField(max_length=30)
    torax = models.CharField(max_length=30)
    abdomen = models.CharField(max_length=30)
    observaciones = models.TextField(max_length=400)
    diagnostico = models.TextField(max_length=400)
    tratamiento = models.TextField(max_length=400)


class Observaciones_Generales(models.Model):
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey('inventario.Trabajador')
    fecha = models.DateTimeField()
    observacion = models.TextField(max_length=300)



#TODO: Agregar Ficha hospital
class Ficha_Hospital(models.Model):
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey('inventario.Trabajador')

#TODO: arreglar estado_pago choices
class Peluqueria(models.Model):
    ESTADO_CHOICES = (
        ('Reservado','Reservado'),
        ('Ingresado','Ingresado'),
        ('Listo para retirar','Listo'),
        ('Retirado','Retirado'),
    )
    mascota = models.ForeignKey(Mascota)
    peluquera = models.ForeignKey('inventario.Trabajador')
    estado = models.CharField(max_length=30,choices=ESTADO_CHOICES)
    descripcion = models.CharField(max_length=100)
    fecha_ingreso = models.DateTimeField(blank=True)
    fecha_retiro = models.DateTimeField(blank=True)
