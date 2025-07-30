# users/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import PerfilUsuario
from .forms import PerfilUsuarioForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cuenta creada exitosamente! Ahora podés iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def perfil_usuario(request):
    perfil = PerfilUsuario.objects.get(user=request.user)
    return render(request, 'users/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, created = PerfilUsuario.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')  # Nombre del path de la vista de perfil
    else:
        form = PerfilUsuarioForm(instance=perfil)

    return render(request, 'users/editar_perfil.html', {'form': form})

