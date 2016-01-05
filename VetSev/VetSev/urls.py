"""VetSev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from inventario import views as i_views
from clinica import views as c_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clientes/info_cliente', i_views.info_cliente, name='info_cliente'),
    url(r'^clientes/nuevo_cliente', i_views.nuevo_cliente, name='nuevo_cliente'),
    url(r'^clientes/nueva_mascota', c_views.nueva_mascota, name='nueva_mascota'),
    url(r'^clientes/modificar_cliente', i_views.modificar_cliente, name='modificar_cliente'),
    url(r'^clientes', i_views.clientes, name='clientes'),
    url(r'^mascotas/info_mascota', c_views.mascota, name='mascotas'),
    url(r'^mascotas/ingresar_consulta', c_views.ingresar_consulta, name='ingresar_consulta'),
    url(r'^mascotas/suscribir', c_views.suscribir_mascota, name='suscribir'),
    url(r'^mascotas', c_views.mascotas, name='mascotas'),
    url(r'^', i_views.hogar, name='home'),

]
