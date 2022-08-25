import os
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,redirect
from .forms import CreacionDeUsuario
from django.contrib.auth import authenticate, login


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