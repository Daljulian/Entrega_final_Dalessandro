# users/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import PerfilUsuario
from .forms import PerfilUsuarioForm, UserUpdateForm
from django.contrib.auth.models import User

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
        form_usuario = UserUpdateForm(request.POST, instance=request.user)
        form_perfil = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)

        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            form_perfil.save()
            return redirect('perfil_usuario')
    else:
        form_usuario = UserUpdateForm(instance=request.user)
        form_perfil = PerfilUsuarioForm(instance=perfil)

    return render(request, 'users/editar_perfil.html', {
        'form_usuario': form_usuario,
        'form_perfil': form_perfil
})