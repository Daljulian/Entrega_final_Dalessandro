# users/urls.py
from . import views
from .views import editar_perfil
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import perfil_usuario

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    
]