from django.urls import path
from . import views

app_name = 'appJuegalo'

urlpatterns = [
    path('', views.home, name='home'),
    path('crear-cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('login/', views.login_view, name='login'),
]