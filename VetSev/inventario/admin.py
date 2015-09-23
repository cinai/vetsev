from django.contrib import admin

from .models import *

class ClienteAdmin(admin.ModelAdmin):
    pass

class IngresoAdmin(admin.ModelAdmin):
    pass

class CajaAdmin(admin.ModelAdmin):
    pass

class ItemProductosAdmin(admin.ModelAdmin):
    pass

class InventarioProductoAdmin(admin.ModelAdmin):
    pass

class TrabajadorAdmin(admin.ModelAdmin):
    pass

class EgresoProductosAdmin(admin.ModelAdmin):
    pass

class VentaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Ingreso, IngresoAdmin)
admin.site.register(Caja,CajaAdmin)
admin.site.register(Item_Productos, ItemProductosAdmin)
admin.site.register(Inventario_Producto, InventarioProductoAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Egreso_Productos, EgresoProductosAdmin)
admin.site.register(Venta, VentaAdmin)
