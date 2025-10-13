from rest_framework import serializers
from .models import Juego, Genero, Plataforma

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'id_rawg', 'nombre', 'slug']

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = ['id', 'id_rawg', 'nombre', 'slug']

class JuegoSerializer(serializers.ModelSerializer):
    generos = GeneroSerializer(many=True, read_only=True)
    plataformas = PlataformaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Juego
        fields = [
            'id', 'id_rawg', 'nombre', 'slug',
            'descripcion', 'imagen_principal',
            'fecha_lanzamiento', 'rating',
            'metacritic', 'generos', 'plataformas',
            'precio', 'stock', 'disponible'
        ]