from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import *
from inventario.models import *


def hogar(request):
	ingresos = Ingreso.objects.all().order_by('-id')
	return render_to_response('index.html',{'navbar':'navbar.html','template_included':'caja.html','ingresos':ingresos},)


def clientes(request):
	clientes = Cliente.objects.all()
	return render(request,'index.html',{'clientes':clientes,'navbar':'navbar.html','template_included':'clientes.html'},)

## TODO: debiese mostrar información de pago 
def info_cliente(request):
	cliente = Cliente.objects.get(pk=request.GET['id'])
	return render(request,'info_cliente.html',{'cliente':cliente,'navbar':'navbar.html'})


def mascotaForm(mascota, cliente):
	if mascota.is_valid():
		try:
			nombre = mascota.cleaned_data['nombre']
			fecha_nac = mascota.cleaned_data['fecha_nacimiento']
			especie = mascota.cleaned_data['especie']
			raza = mascota.cleaned_data['raza']
			color = mascota.cleaned_data['color']
			sexo = mascota.cleaned_data['sexo']
			suscrito = mascota.cleaned_data['suscrito']
		except Exception as e:
			print("error en parte del formulario mascota")
			return 0
		try:
			mascota = Mascota(cliente=cliente,nombre=nombre,fecha_nacimiento=fecha_nac,especie=especie,raza=raza, color=color, sexo=sexo,suscrito=suscrito)
			mascota.save()
			return 1
		except Exception as e:
			print("error al guardar mascota")
			return 0
	else:
		print("error en formulario mascota")
		print(mascota.errors)
		return 0


def nuevo_cliente(request):
	# create a form instance and populate it with data from the request:				
	cliente_form = ClienteForm(request.POST or None, prefix="cliente")		
	mascotas_form = MascotaFormSet(request.POST or None, prefix="mascotas")    
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# check whether it's valid:
		if cliente_form.is_valid():
			if Cliente.objects.filter(rut=cliente_form.cleaned_data['rut']).exists():
				 return render(request,'nuevo_cliente.html',{'agregar_cliente_success':False,'navbar':'navbar.html','cliente_form':cliente_form, 'mascotas_form':mascotas_form})
			cliente = cliente_form.save()
			for mascota in mascotas_form:
				retorno = mascotaForm(mascota, cliente)
				if retorno == 0:
					cliente.delete()
					return render(request,'nuevo_cliente.html',{'agregar_mascota_success':False,'navbar':'navbar.html','cliente_form':cliente_form, 'mascotas_form':mascotas_form})
			#TODO: if suscrito = true then crear pago suscripcion
			return render(request,'info_cliente.html',{'cliente':cliente,'navbar':'navbar.html','agregar_cliente_success':True})
	# if a GET (or any other method) we'll create a blank form
	return render(request,'nuevo_cliente.html',{'navbar':'navbar.html','cliente_form':cliente_form, 'mascotas_form':mascotas_form})


def modificar_cliente(request):
	return render_to_response('modificar_cliente.html',{'navbar':'navbar.html'},)