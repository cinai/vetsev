from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response, render
from django.utils import timezone
from inventario.models import Cliente, Ingreso, Caja
from inventario.forms import *
from inventario.views import mascotaForm
from clinica.forms import ConsultaForm
from clinica.models import Mascota, Consulta
import json

def nueva_mascota(request):
	mascotas_form = MascotaFormSet(request.POST or None, prefix="mascotas")    
	cliente = Cliente.objects.get(pk=request.GET['id'])
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# check whether it's valid:
		n_mascotas = 0
		for mascota in mascotas_form:
			retorno = mascotaForm(mascota, cliente)
			n_mascotas += 1
			if retorno == 0:
				return render(request,'info_cliente.html',{'agregar_mascota_success':False,'navbar':'navbar.html','mascotas_form':mascotas_form})
		#TODO: if suscrito = true then crear pago suscripcion
		if n_mascotas > 1:
			return render(request,'info_cliente.html',{'cliente':cliente,'navbar':'navbar.html','agregar_mascota_success':True})
		return render(request,'info_cliente.html',{'cliente':cliente,'navbar':'navbar.html','agregar_mascota_succes':True})
	# if a GET (or any other method) we'll create a blank form
	return render(request,'nueva_mascota.html',{'navbar':'navbar.html','cliente':cliente, 'mascotas_form':mascotas_form})

def mascotas(request):
	mascotas = Mascota.objects.all()
	consulta_form = ConsultaForm(None, prefix="consulta")
	return render(request,'index.html',{'consulta_form':consulta_form,'mascotas':mascotas,'navbar':'navbar.html','template_included':'mascotas.html'},)

#Deberia mostrar info de calendarios
def mascota(request):
	mascota = Mascota.objects.get(pk=request.GET['id'])
	return render(request,'info_mascota.html',{'mascota':mascota,'navbar':'navbar.html'},)

#Deberia mostrar info de calendarios
def suscribir_mascota(request):
	mascota = Mascota.objects.get(pk=request.GET['id'])
	mascota.suscrito = True
	mascota.save()
	message = "La mascota fue suscrita correctamente"
	return HttpResponse(message)

#TODO: arreglar que ingreso no necesite nada mas en el modelo, ingresar cajas para
#agarrar la ultima creada
def ingresar_consulta(request):
	try:
		mascota = Mascota.objects.get(pk=request.POST['id'])
	except Exception as e:
		message = "mascota get no funciona" + str(request.POST['id'])
		print (message)
		return HttpResponse(message)
	try:
		consulta_form = ConsultaForm(request.POST, prefix="consulta")
	except Exception as e:
		message = "mascota consultaform no funciona"
		print (message)
		return HttpResponse(message)
	# if this is a POST request we need to process the form data
	message = "No ha sido posible ingresar la consulta, por favor intente nuevamente."
	if request.method == 'POST':
		# check whether it's valid:
		if consulta_form.is_valid():
			try:
				monto = consulta_form.cleaned_data['monto']
				veterinario = consulta_form.cleaned_data['veterinario']
				fecha = timezone.now()
				caja = Caja.objects.last()
				ingreso = Ingreso(cliente = mascota.cliente,fecha=fecha,caja=caja)
				ingreso.save()
			except Exception as e:
				print (str(e))
				return HttpResponse(message)
			#TODO: if suscrito = true then crear pago suscripcion
			try:
				consulta = Consulta(monto=monto, veterinario=veterinario, ingreso= ingreso, mascota=mascota, fecha_ingreso=fecha)
				consulta.save()
				message = "Se ha generado el pago de la consulta correctamente"
				return HttpResponse(message)
			except Exception as e:
				ingreso.delete()
				print (str(e))
		else:
			print(consulta_form.errors)
	else:
		return mascotas(request)
	return HttpResponse(message)

def crear_mascota(request):
    return render_to_response('index.html',{'navbar':'navbar.html','template_included':'caja.html'},)
