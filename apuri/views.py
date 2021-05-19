from django.shortcuts import render

def post_list(request):
    return render(request, 'Portal.html', {})

def Inicio(request):
    return render(request, 'Inicio.html', {})

