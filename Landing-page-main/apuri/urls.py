from django.urls import path
from . import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('Login/', views.Login ),
    path('Recuperacion/', views.Recuperacion),
    path('Re_contraseña/',views.Re_contraseña),
    path('inicio/', views.inicio, name='inicio'),
    path('', views.Portal, name='Portal'),
    path('perfil/', views.perfil, name='perfil'),
]