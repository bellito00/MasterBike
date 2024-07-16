"""
URL configuration for Otaku_od project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Aplicacion import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    path('administracion/', administracion, name='administracion'),
    path('mantenciones/', mantenciones, name='mantenciones'),
    path('agregarmantencion/', agregarmantencion, name='agregarmantencion'),
    path('modificarmantencion/<id>/', modificarmantencion, name='modificarmantencion'),
    path('eliminarmantencion/<id>/', eliminarmantencion, name='eliminarmantencion'),
    path('agregartecnico/', agregartecnico, name='agregartecnico'),
    path('agregarsucursal/', agregarsucursal, name='agregarsucursal'),
    path('historial/', historial, name='historial'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)