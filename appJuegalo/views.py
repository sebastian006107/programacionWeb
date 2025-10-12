from django.shortcuts import render, redirect
from .models import Juego, Plataforma, Perfil, Genero
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


# API REST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import JuegoSerializer, GeneroSerializer



@api_view(['GET', 'POST'])
@permission_classes([])
def api_juegos(request):
    if request.method == 'GET':
        # GET es público - cualquiera puede ver
        juegos = Juego.objects.all()
        serializer = JuegoSerializer(juegos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # POST solo para admin
        if not request.user.is_authenticated:
            return Response(
                {'error': 'Debes iniciar sesión'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        if not request.user.is_staff:
            return Response(
                {'error': f'Usuario {request.user.username} no es admin. is_staff={request.user.is_staff}'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = JuegoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([])  # ← AGREGAR ESTA LÍNEA
def api_generos(request):
    generos = Genero.objects.all()
    serializer = GeneroSerializer(generos, many=True)
    return Response(serializer.data)






@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([])
def api_juego_detalle(request, pk):
    try:
        juego = Juego.objects.get(pk=pk)
    except Juego.DoesNotExist:
        return Response({'error': 'Juego no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # GET es público
        serializer = JuegoSerializer(juego)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # PUT solo para admin
        if not request.user.is_staff:
            return Response(
                {'error': 'Solo administradores pueden editar juegos'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = JuegoSerializer(juego, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # DELETE solo para admin
        if not request.user.is_staff:
            return Response(
                {'error': 'Solo administradores pueden eliminar juegos'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        juego.delete()
        return Response({'mensaje': 'Juego eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)