from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory, formset_factory, modelformset_factory
from django.forms.extras.widgets import SelectDateWidget
from inventario.models import Cliente
from clinica.models import Mascota

class ClienteForm(ModelForm):	
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre...'}))
	rut = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese rut'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese teléfono'}))
	telefono2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese teléfono'}))
	direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese dirección...'}))
	comuna = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese comuna'}))
	mail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingrese email'}))

	class Meta:
		model = Cliente
		exclude = ['fecha_ingreso']
		

class MascotaForm(ModelForm):
	fecha_nacimiento = forms.DateField(input_formats=['%d/%m/%y', '%d/%m/%Y'])

	class Meta:
		model = Mascota
		exclude = ['cliente','fecha_ingreso']

MascotaFormSet = formset_factory(MascotaForm, extra=1)
