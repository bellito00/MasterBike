from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from functools import wraps
from django.db import transaction
from django.core.exceptions import ValidationError


from .models import *
from .forms import *
from .enumeraciones import *

# Decorador para restringir vistas a administradores
def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Vista para el índice

def index(request):

    
    return render(request, 'Otaku_ody/index.html')
# Vista para preguntas frecuentes
def preguntas(request):
    return render(request, 'Otaku_ody/preguntas.html')



# Vistas para administración
@admin_required
def administracion(request):
    return render(request, 'Otaku_ody/administracion.html')


@admin_required
def mantenciones(request):
    mantenciones = Mantencion.objects.all()
    paginator = Paginator(mantenciones, 4)

    page = request.GET.get('page')
    try:
        mantenciones_paginados = paginator.get_page(page)
    except PageNotAnInteger:
        mantenciones_paginados = paginator.get_page(1)
    except EmptyPage:
        mantenciones_paginados = paginator.get_page(paginator.num_pages)

    return render(request, 'Otaku_ody/mantenciones.html', {'entity': mantenciones_paginados, 'paginator': paginator})

@admin_required
def agregartecnico(request):
    form = Tecnico()
    if request.method == 'POST':
        form = Tecnico(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tecnico agregado')
            return redirect('mantenciones')
    return render(request, 'Otaku_ody/agregartecnico.html', {'form': form})

@admin_required
def agregarsucursal(request):
    form = Sucursal()
    if request.method == 'POST':
        form = Sucursal(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sucursal agregada')
            return redirect('mantenciones')
    return render(request, 'Otaku_ody/agregarsucursal.html', {'form': form})

@admin_required
def agregarmantencion(request):
    if request.method == 'POST':
        form = MantencionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantenimiento Agregado')
            return redirect('mantenciones')  # Redirect to the list view
    else:
        form = MantencionForm()

    return render(request, 'Otaku_ody/agregarmantencion.html', {'form': form})

@admin_required
def modificarmantencion(request, id):
    mantencion = get_object_or_404(Mantencion, id=id)
    form = ModificarMantencionForm(instance=mantencion)
    if request.method == 'POST':
        form = ModificarMantencionForm(request.POST, request.FILES, instance=mantencion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantencion Modificada')
            return redirect('mantenciones')
    return render(request, 'Otaku_ody/modificarmantencion.html', {'form': form})

@admin_required
def eliminarmantencion(request, id):
    mantencion = get_object_or_404(Mantencion, id=id)
    if mantencion.imagen:
        mantencion.imagen.delete()
    mantencion.delete()
    messages.warning(request, 'Mantencion Eliminada')
    return redirect('mantenciones')

@login_required
def historial(request):
    # Filtrar pedidos por el usuario actual
    mantencion = Mantencion.objects.filter(usuario=request.user)

    paginator = Paginator(mantencion, 4)

    page = request.GET.get('page')
    try:
        mantencion_paginados = paginator.page(page)
    except PageNotAnInteger:
        mantencion_paginados = paginator.page(1)
    except EmptyPage:
        mantencion_paginados = paginator.page(paginator.num_pages)

    return render(request, 'Otaku_ody/historial.html', {'entity': mantencion_paginados, 'paginator': paginator})

# Vistas para autenticación
def login_view(request):
    return render(request, 'registration/login.html')

def registro(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect('index')
    return render(request, 'registration/registro.html', {'form': form})
