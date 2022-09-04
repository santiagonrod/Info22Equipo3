import os
from tkinter.tix import Form
from turtle import title
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,redirect, get_object_or_404
from .forms import CreacionDeUsuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from apps.blog.forms import FormPost, UserForm
from .models import post
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView


# Create your views here.
'''
def post_list(request):
    return render(request, os.path.join(settings.BASE_DIR, '/templates/index.html'), {})
'''
location = os.path.join(settings.BASE_DIR, 'templates/post_list.html')

def inicio(request):
    get_all_posts = post.objects.all().order_by('-created_date')[:3]
    context = {
        'posts':get_all_posts
    }
    return render(request, os.path.join(settings.BASE_DIR, 'templates/index.html'), context)

def post_list(request):
    get_all_posts = post.objects.all().order_by('-created_date')
    context = {
        'posts':get_all_posts
    }
    return render(request, location, context)

def detail_view(request, id):
    context = {}
    context['post'] = post.objects.get(pk=id)

    return render(request, 'post.html', context)

'''def perfil_usuario(request, id):
    context = {}
    context['user'] = User.objects.get(pk=id)

    return render(request, 'perfil_usuario.html', context)
'''

def perfil_usuario(request, id):
    user = User.objects.get(id=id)
    data = {
        'form': UserForm(instance=user)
  }
    if request.method == "POST":
        form = UserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            data['form'] = form
    return render(request, 'perfil_usuario.html', data)


def a_post(request):
    return render(request, os.path.join(settings.BASE_DIR, 'templates/post.html'), {})

def registro(request):
    data = {
        'form': CreacionDeUsuario()
    }

    if request.method == 'POST':
        formulario = CreacionDeUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect (to="inicio")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def crear_post(request):
    if request.method == "POST":
        form = FormPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user.id
            post.save()
            titulo = form.cleaned_data.get("title")
            messages.success(request, f"El post {title} se ha creado correctamente")
            return redirect(to="post_list")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
    form = FormPost()
    return render(request, "crear_post.html", {"form": form})


def sobre_nosotros(request):
     return render(request, 'sobre_nos.html')

def asociarse(request):
    return render(request, 'asociarse.html')


def editar_post(request, id):
    Post = post.objects.get(id=id)
    data = {
        'form': FormPost(instance=Post)
  }
    if request.method == "POST":
        form = FormPost(data=request.POST, instance=Post)
        if form.is_valid():
            form.save()
            data['form'] = form
    return render(request, 'editar.html', data)




def eliminar_post(request, id):
    Post = post.objects.get(id=id)
    Post.delete()
    return redirect(to= 'post_list')