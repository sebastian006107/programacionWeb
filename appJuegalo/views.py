from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')  

def crear_cuenta(request):
    return render(request, 'crear-cuenta.html')  


def login_view(request):
    return render(request, 'login.html')