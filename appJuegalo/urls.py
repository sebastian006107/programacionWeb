from django.urls import path
from . import views

app_name = 'appJuegalo'

urlpatterns = [
    path('', views.home, name='home'),
    path('crear-cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('login/', views.login_view, name='login'),
    path('juegos/<int:game_id>/', views.detalle_juego, name='detalle_juego'), 
    path('pc/', views.pc, name='pc'),
    path('playstation/', views.playstation, name='playstation'),
]