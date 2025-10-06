import requests
from datetime import datetime
from .models import Juego, Genero, Plataforma

API_KEY = '646d5d8f63a44be69214f55e42654973'
BASE_URL = 'https://api.rawg.io/api'


def obtener_juegos_api(plataforma_id=None, cantidad=12):
    url = f"{BASE_URL}/games"
    params = {
        'key': API_KEY,
        'page_size': cantidad,
        'ordering': '-added',
        'metacritic': '80,100'
    }
    
    if plataforma_id:
        params['platforms'] = plataforma_id
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar API: {e}")
        return []


def guardar_juego_bd(data):
    fecha_lanzamiento = None
    if data.get('released'):
        try:
            fecha_lanzamiento = datetime.strptime(data['released'], '%Y-%m-%d').date()
        except:
            pass
    
    juego, created = Juego.objects.update_or_create(
        id_rawg=data['id'],
        defaults={
            'nombre': data.get('name', ''),
            'slug': data.get('slug', ''),
            'descripcion': data.get('description_raw', ''),
            'imagen_principal': data.get('background_image', ''),
            'imagen_adicional': data.get('background_image_additional', ''),
            'fecha_lanzamiento': fecha_lanzamiento,
            'rating': data.get('rating', 0),
            'metacritic': data.get('metacritic'),
            'sitio_web': data.get('website', ''),
        }
    )
    
    if data.get('genres'):
        for genero_data in data['genres']:
            genero, _ = Genero.objects.get_or_create(
                id_rawg=genero_data['id'],
                defaults={
                    'nombre': genero_data['name'],
                    'slug': genero_data['slug']
                }
            )
            juego.generos.add(genero)
    
    if data.get('platforms'):
        for plat_data in data['platforms']:
            plataforma, _ = Plataforma.objects.get_or_create(
                id_rawg=plat_data['platform']['id'],
                defaults={
                    'nombre': plat_data['platform']['name'],
                    'slug': plat_data['platform']['slug']
                }
            )
            juego.plataformas.add(plataforma)
    
    return juego


def sincronizar_juegos(plataforma_id=None, cantidad=12):
    juegos_api = obtener_juegos_api(plataforma_id, cantidad)
    juegos_guardados = []
    
    for juego_data in juegos_api:
        juego = guardar_juego_bd(juego_data)
        juegos_guardados.append(juego)
    
    return juegos_guardados


def obtener_detalle_juego_api(game_id):
    url = f"{BASE_URL}/games/{game_id}"
    params = {'key': API_KEY}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar API: {e}")
        return None