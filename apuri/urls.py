from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('Login/', views.Login),
    path('Recuperacion/', views.Recuperacion),
    path('calendario.html', views.calendario, name='calendario'),
]