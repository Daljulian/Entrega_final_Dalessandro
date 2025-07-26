from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Categoria
from .forms import PostForm, ComentarioForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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

