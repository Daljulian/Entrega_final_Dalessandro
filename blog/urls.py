from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
    
]