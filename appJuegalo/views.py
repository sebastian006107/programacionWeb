from django.shortcuts import render, redirect
from .models import Juego, Plataforma, Perfil
from .services import sincronizar_juegos, obtener_detalle_juego_api, guardar_juego_bd
from .forms import RegistroForm
from django.contrib.auth import authenticate, login

# ... resto de tu código ...
def home(request):
    juegos = Juego.objects.all()[:12]
    
    if juegos.count() < 12:
        sincronizar_juegos(cantidad=12)
        juegos = Juego.objects.all()[:12]
    
    return render(request, 'index.html', {'juegos': juegos})




def crear_cuenta(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            Perfil.objects.create(
                user=user,
                telefono=form.cleaned_data.get('telefono'),
                direccion=form.cleaned_data.get('direccion')
            )
            
            return redirect('appJuegalo:login')
    else:
        form = RegistroForm()
    
    return render(request, 'crear-cuenta.html', {'form': form})








def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('appJuegalo:home')
        else:
            error = "Usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error': error})
    
    return render(request, 'login.html')









def pc(request):
    plataforma_pc = Plataforma.objects.filter(id_rawg=4).first()
    
    if plataforma_pc:
        juegos = plataforma_pc.juegos.all()[:30]
    else:
        juegos = Juego.objects.none()
    
    if juegos.count() < 30:
        sincronizar_juegos(plataforma_id=4, cantidad=30)
        plataforma_pc = Plataforma.objects.filter(id_rawg=4).first()
        if plataforma_pc:
            juegos = plataforma_pc.juegos.all()[:30]
    
    return render(request, 'pc.html', {'juegos': juegos})


def playstation(request):
    plataformas_ps = Plataforma.objects.filter(id_rawg__in=[18, 187, 16])
    
    if plataformas_ps.exists():
        juegos = Juego.objects.filter(plataformas__in=plataformas_ps).distinct()[:30]
    else:
        juegos = Juego.objects.none()
    
    if juegos.count() < 30:
        sincronizar_juegos(plataforma_id='18,187,16', cantidad=30)
        plataformas_ps = Plataforma.objects.filter(id_rawg__in=[18, 187, 16])
        if plataformas_ps.exists():
            juegos = Juego.objects.filter(plataformas__in=plataformas_ps).distinct()[:30]
    
    return render(request, 'playstation.html', {'juegos': juegos})


def detalle_juego(request, game_id):
    juego = Juego.objects.filter(id_rawg=game_id).first()
    
    if not juego:
        data = obtener_detalle_juego_api(game_id)
        if data:
            juego = guardar_juego_bd(data)
    
    return render(request, 'detalle-juego.html', {'juego': juego})


