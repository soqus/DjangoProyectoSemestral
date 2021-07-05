"""Mecanicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('core.urls')),
    path ('aceptada', include('core.urls')),
    path ('fichatecnicaL1', include('core.urls')),
    path ('index', include('core.urls')),
    path ('inicioadministrador', include('core.urls')),
    path ('iniciosesion', include('core.urls')),
    path ('iniciousuario', include('core.urls')),
    path ('mensajeregistroL1', include('core.urls')),
    path ('Nuestrosmecanicos', include('core.urls')),
    path ('perfiladministrador', include('core.urls')),
    path ('perfilusuario', include('core.urls')),
    path ('peticiones', include('core.urls')),
    path ('rechazada', include('core.urls')),
    path ('registrouduario', include('core.urls')),
    path ('trabajos_realizados', include('core.urls')),
    path ('verpeticion', include('core.urls')),
    

    
    
]
