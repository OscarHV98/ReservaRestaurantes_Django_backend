from django.contrib import admin
from .models import Cliente, Mesa, Reservacion, Categoria, Plato, Restaurante

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'correo', 'telefono', 'is_active', 'is_staff')
    search_fields = ('username', 'nombre', 'correo', 'telefono')  # Campos para búsqueda
    list_filter = ('is_active', 'is_staff')  # Filtros por estado
    ordering = ('username',)

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'telefono')  # Campos para búsqueda
    ordering = ('nombre',)

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'capacidad', 'ubicacion', 'disponible', 'restaurante')
    search_fields = ('numero', 'restaurante__nombre')  # Campos para búsqueda
    list_filter = ('disponible', 'restaurante')  # Filtros
    ordering = ('restaurante', 'numero')

@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'mesa', 'fecha_hora', 'estado', 'numero_de_personas')
    search_fields = ('cliente__username', 'mesa__numero', 'mesa__restaurante__nombre')  # Campos para búsqueda
    list_filter = ('estado', 'mesa__restaurante')  # Filtros
    ordering = ('-fecha_hora',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'restaurante', 'precio', 'disponible', 'categoria')
    search_fields = ('nombre', 'restaurante__nombre', 'categoria__nombre')  # Campos para búsqueda
    list_filter = ('disponible', 'restaurante', 'categoria')  # Filtros
    ordering = ('restaurante', 'nombre')