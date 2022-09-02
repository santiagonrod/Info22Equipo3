import os
from tkinter.tix import Form
from turtle import title
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,redirect, get_object_or_404
from .forms import CreacionDeUsuario
from django.contrib.auth import authenticate, login
from apps.blog.forms import FormPost
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

'''class VistaPost(DetailView):
    model = post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(post,)
'''



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