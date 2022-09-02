from tokenize import Name
from unicodedata import name
from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post_list/', views.post_list, name='post_list'),
    '''path('post/<int:id>/', VistaPost.as_view(), name='post'),'''
    path('registro/',views.registro, name='registro'),
    path('nuevo_post/', views.crear_post, name='nuevo_post'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('asociarse/', views.asociarse, name= 'asociarse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
