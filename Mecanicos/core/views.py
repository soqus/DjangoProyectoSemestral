from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def aceptada(request):
    return render (request ,'core/aceptada.html')

def fichatecnicaL1(request):
    return render (request ,'core/fichatecnicaL1.html')

def inicioadministrador(request):
    return render (request ,'core/inicioadministrador.html')

def iniciosesion(request):
    return render (request ,'core/iniciosesion.html')

def iniciousuario(request):
    return render (request ,'core/iniciousuario.html')

def mensajeregistroL1(request):
    return render (request ,'core/mensajeregistroL1.html')

def Nuestrosmecanicos(request):
    return render (request ,'core/Nuestrosmecanicos.html')

def perfiladministrador(request):
    return render (request ,'core/perfiladministrador.html')

def perfilusuario(request):
    return render (request ,'core/perfilusuario.html')

def peticiones(request):
    return render (request ,'core/peticiones.html')

def rechazada(request):
    return render (request ,'core/rechazada.html')

def registrousuario(request):
    return render (request ,'core/registrousuario.html')

def trabajos_realizados(request):
    return render (request ,'core/trabajos_realizados.html')

def verpeticion(request):
    return render (request ,'core/verpeticion.html')

