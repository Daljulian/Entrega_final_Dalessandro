from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/eliminar/', views.eliminar_post, name='eliminar_post'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]