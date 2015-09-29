from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response


def clientes(request):
    return render_to_response('index.html',{'navbar':'navbar.html','template_included':'clientes.html'},)


def nuevo_cliente(request):
	return render_to_response('nuevo_cliente.html',{'navbar':'navbar.html'},)


def suscribir_cliente(request):
	return render_to_response('suscribir_cliente.html',{'navbar':'navbar.html'},)


def modificar_cliente(request):
	return render_to_response('modificar_cliente.html',{'navbar':'navbar.html'},)