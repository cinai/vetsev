# -*- coding: utf-8 -*-
from django.db import models
from VetSev.inventario.models import Ingreso, Cliente, Trabajador


ESTADO_PAGO_CHOICES = (
    ('Pendiente','Pendiente'),
    ('Parcial','Parcial'),
    ('Pagado','Pagado'),
)


class Mascota(models.Model):
    cliente = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    color = models.CharField(max_length=20)


class Consulta(models.Model):
    monto = models.IntegerField(default=7500)
    fecha = models.DateTimeField()
    ingreso = models.ForeignKey(Ingreso)
    mascota = models.ForeignKey(Mascota)


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


#TODO: pensar mejor eventos y calendarios
class Evento_Mascota(models.Model):
    ESTADO_CHOICES = (
        ('Sin Avisar','Sin Avisar'),
        ('Avisado','Avisado'),
        ('Confirmado','Confirmado'),
        ('En curso','En curso'),
    )
    TIPO_CHOICES = (
        ('Baño','Baño'),
        ('Vacuna','Vacuna'),
        ('Hospitalización','Hospitalización'),
    )
    mascota = models.ForeignKey(Mascota)
    estado = models.CharField(max_length=30,choices=ESTADO_CHOICES)
    tipo = models.CharField(max_length=20,choices=TIPO_CHOICES)
    fecha = models.DateTimeField()

#TODO: completar ficha clinica
class Ficha_Clinica:
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey(Trabajador)


class Observaciones_Generales:
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey(Trabajador)
    observacion = models.TextField(max_length=300)


#TODO: estado del pago
class Hotel:
    ESTADO_CHOICES = (
        ('Reservado','Reservado'),
        ('Alojado','Alojado'),
        ('Retirado','Retirado'),
    )
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey(Trabajador)
    estado = models.CharField(max_length=30,choices=ESTADO_CHOICES)
    fecha_ingreso = models.DateTimeField(blank=True)
    fecha_retiro = models.DateTimeField(blank=True)


class Hospitalizacion:
    ESTADO_CHOICES = (
        ('Reservado','Reservado'),
        ('Alojado','Alojado'),
        ('Retirado','Retirado'),
        ('Fallecido','Fallecido'),
    )
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey(Trabajador)
    diagnostico = models.CharField(max_length=150)
    estado = models.CharField(max_length=30,choices=ESTADO_CHOICES)
    estado_pago = models.CharField(max_length=14,choices=ESTADO_PAGO_CHOICES)
    fecha_ingreso = models.DateTimeField(blank=True)
    fecha_retiro = models.DateTimeField(blank=True)


#TODO: Agregar Ficha hospital
class Ficha_Hospital:
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey(Trabajador)

#TODO: arreglar estado_pago choices
class Peluqueria:
    ESTADO_CHOICES = (
        ('Reservado','Reservado'),
        ('Alojado','Alojado'),
        ('Retirado','Retirado'),
    )
    mascota = models.ForeignKey(Mascota)
    trabajador = models.ForeignKey(Trabajador)
    estado = models.CharField(max_length=30,choices=ESTADO_CHOICES)
    fecha_ingreso = models.DateTimeField(blank=True)
    fecha_retiro = models.DateTimeField(blank=True)
