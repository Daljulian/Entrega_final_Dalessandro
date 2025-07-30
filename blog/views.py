from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Categoria
from .forms import PostForm, ComentarioForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden

#from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm


#def register(request):
    #form = UserCreationForm()
    #if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('login')
    #return render(request, 'users/register.html', {'form': form})

def index(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(titulo__icontains=query) | Q(contenido__icontains=query))
    else:
        posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'blog/index.html', {'posts': posts})

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentarios.all()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('detalle_post', post_id=post.id)
    else:
        form = ComentarioForm()
    return render(request, 'blog/detalle_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })

def buscar_post(request):
    query = request.GET.get('q', '')  # obtener el texto del input de búsqueda
    resultados = []
    if query:
        resultados = Post.objects.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        ).distinct()
    return render(request, 'blog/buscar.html', {'resultados': resultados, 'query': query})

@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.autor != request.user:
        return HttpResponseForbidden("No tenés permiso para editar este post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/editar_post.html', {'form': form, 'post': post})

@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.autor != request.user:
        return HttpResponseForbidden("No tenés permiso para eliminar este post.")

    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')  # O la vista principal
    return render(request, 'blog/confirmar_eliminacion.html', {'post': post})