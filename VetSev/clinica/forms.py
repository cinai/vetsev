from django import forms
from django.forms import ModelForm
from inventario.models import Cliente
from clinica.models import Mascota, Consulta, Hospitalizacion

class ConsultaForm(ModelForm):	
	class Meta:
		model = Consulta
		exclude = ['fecha_ingreso','ingreso','mascota']

		
class HospitalizacionForm(ModelForm):	
	class Meta:
		model = Hospitalizacion
		exclude = ['fecha_ingreso','ingreso','mascota']


