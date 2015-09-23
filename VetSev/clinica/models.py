# -*- coding: utf-8 -*-
from django.db import models
from inventario.models import Ingreso, Cliente

class Mascota(models.Model):
    cliente = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=100)

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