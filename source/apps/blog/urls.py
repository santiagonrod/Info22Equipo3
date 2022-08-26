from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post', views.post_list, name='post_list'),
    path('registro/',views.registro, name='registro'),
    path('post_crear/', views.crear_post, name='crear_post')
]