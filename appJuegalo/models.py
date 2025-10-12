from django.db import models

class Genero(models.Model):
    id_rawg = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Géneros"
    
    def __str__(self):
        return self.nombre


class Plataforma(models.Model):
    id_rawg = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Juego(models.Model):
    id_rawg = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    descripcion = models.CharField(max_length=2000, blank=True, null=True)
    imagen_principal = models.URLField(max_length=500, blank=True, null=True)
    imagen_adicional = models.URLField(max_length=500, blank=True, null=True)
    fecha_lanzamiento = models.DateField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    metacritic = models.IntegerField(blank=True, null=True)
    sitio_web = models.URLField(max_length=500, blank=True, null=True)
    
    generos = models.ManyToManyField(Genero, related_name='juegos')
    plataformas = models.ManyToManyField(Plataforma, related_name='juegos')
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-rating', '-metacritic']
    
    def __str__(self):
        return self.nombre