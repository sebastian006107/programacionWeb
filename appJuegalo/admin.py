from django.contrib import admin
from .models import Genero, Plataforma, Juego, Perfil

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'id_rawg']
    search_fields = ['nombre']

@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'id_rawg']
    search_fields = ['nombre']

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rating', 'metacritic', 'fecha_lanzamiento']
    search_fields = ['nombre']
    list_filter = ['generos', 'plataformas']
    filter_horizontal = ['generos', 'plataformas']


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['user', 'telefono', 'direccion']