from django.contrib import admin
from .models import Producto, Categoria
from .models import Publicacion

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'usuario', 'precio', 'fecha_publicacion')
    search_fields = ('producto__nombre', 'usuario__username')
    list_filter = ('producto__categoria',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio')  # Muestra columnas clave
    search_fields = ('nombre',)                             # Habilita búsqueda por nombre
    list_filter = ('categoria',)                            # Filtro lateral por categoría

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Visualización de categorías en admin

# Personalización del panel de administración
admin.site.site_header = "Administración de AgroRegistro"
admin.site.site_title = "AgroRegistro Admin"
admin.site.index_title = "Panel de control"
