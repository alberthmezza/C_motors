from django.contrib import admin
from .models import Marca, Categoria, Proveedor, Producto, Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "valor_ingreso"]
    list_editable = ["nombre"]
    search_fields = ["nombre"]
    list_filter = ["estado"]

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)