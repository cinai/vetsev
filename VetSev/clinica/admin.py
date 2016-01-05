from django.contrib import admin

from .models import *
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    pass

class ConsultaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Consulta, ConsultaAdmin)
