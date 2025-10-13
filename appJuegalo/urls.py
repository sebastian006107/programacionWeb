from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'appJuegalo'

urlpatterns = [
    path('', views.home, name='home'),
    path('crear-cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='appJuegalo:home'), name='logout'),
    path('juegos/<int:game_id>/', views.detalle_juego, name='detalle_juego'), 
    path('pc/', views.pc, name='pc'),
    path('playstation/', views.playstation, name='playstation'),
    path('xbox/', views.xbox, name='xbox'),
    path('nintendo/', views.nintendo, name='nintendo'),
    
    path('panel-admin/', views.panel_admin, name='panel_admin'),
    
    path('api/juegos/', views.api_juegos, name='api_juegos'),
    path('api/juegos/<int:pk>/', views.api_juego_detalle, name='api_juego_detalle'),
    path('api/generos/', views.api_generos, name='api_generos'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]