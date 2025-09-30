from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')  

def crear_cuenta(request):
    return render(request, 'crear-cuenta.html')  


def login_view(request):
    return render(request, 'login.html')

def detalle_juego(request, game_id):
    return render(request, 'detalle-juego.html', {'game_id': game_id})

def pc(request):
    return render(request, 'pc.html')
def playstation(request):
    return render(request, 'playstation.html')