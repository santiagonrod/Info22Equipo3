import os
from tkinter.tix import Form
from turtle import title
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,redirect
from .forms import CreacionDeUsuario
from django.contrib.auth import authenticate, login
from apps.blog.forms import FormPost


# Create your views here.
'''
def post_list(request):
    return render(request, os.path.join(settings.BASE_DIR, '/templates/index.html'), {})
'''
location = os.path.join(settings.BASE_DIR, 'templates/post.html')

def inicio(request):
    return render(request, os.path.join(settings.BASE_DIR, 'templates/index.html'), {})


def post_list(request):
    return render(request, location, {})

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
            return redirect (to="post_list")
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
            return redirect("post")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
    form = FormPost()
    return render(request, "crear_post.html", {"form": form})


def sobre_nosotros(request):
     return render(request, 'sobre_nos.html')