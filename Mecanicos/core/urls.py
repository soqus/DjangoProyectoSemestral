from django.urls import path
from .views import index, aceptada, fichatecnicaL1, inicioadministrador, iniciosesion,iniciousuario,mensajeregistroL1,Nuestrosmecanicos, perfiladministrador, perfilusuario, peticiones, rechazada, registrousuario, registrousuario, trabajos_realizados, verpeticion


urlpatterns = [
    path('',index, name='index'),
    path('index',index, name='index'),
    path('aceptada',aceptada, name='aceptada'),
    path('fichatecnicaL1',fichatecnicaL1, name='fichatecnicaL1'),
    path('inicioadministrador',inicioadministrador, name='inicioadministrador'),
    path('iniciosesion',iniciosesion, name='iniciosesion'),
    path('iniciousuario',iniciousuario, name='iniciousuario'),
    path('mensajeregistroL1',mensajeregistroL1, name='mensajeregistroL1'),
    path('Nuestrosmecanicos',Nuestrosmecanicos, name='Nuestrosmecanicos'),
    path('perfiladministrador',perfiladministrador, name='perfiladministrador'),
    path('perfilusuario',perfilusuario, name='perfilusuario'),
    path('peticiones',peticiones, name='peticiones'),
    path('rechazada',rechazada, name='rechazada'),
    path('registrousuario',registrousuario, name='registrousuario'),
    path('trabajos_realizados',trabajos_realizados, name='trabajos_realizados'),
    path('verpeticion',verpeticion, name='verpeticion'),
]