from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from apuri.models import Miembro

def post_list(request):
    return render(request, 'Portal.html', {})


def Login(request):

    if request.GET["user"]:
        #mensaje_usu = 'Usuario: %r <br> ' %request.GET["user"]
        email = request.GET["user"]
        usuarios = Miembro.objects.filter(email__exact=email)

        contraseña = request.GET['pass']

        mensaje = 'correo incorrecto'



        for usuario in usuarios:

             if usuario.contraseña == contraseña:

                 institucion = usuario.institucion
                 nombre = usuario.nombre
                 ap_pat = usuario.apellido_pat
                 ap_mat = usuario.apellido_mat
                 mensaje = 'pase_nomas'
                 return render(request, "Inicio.html", {"query": email, "mensaje": mensaje,
                    "contraseña":contraseña, "institucion":institucion, "nombre":nombre ,"ap_pat":ap_pat, "ap_mat":ap_mat })


             elif usuario.contraseña != contraseña:
                 nombre = usuario.nombre
                 mensaje = 'no_flaco'
                 return render(request, "Portal.html", {"query": email, "mensaje": mensaje, "nombre":nombre})

             else :
                 nombre = usuario.nombre
                 mensaje = "no_email"
                 return render(request, "Portal.html", {"query": email, "mensaje": mensaje, "nombre": nombre})


    else:
        mensaje = 'No ingresaste nada bruh'

    return render(request, "Portal.html", { "mensaje": mensaje})

def Recuperacion(request):

    if request.GET["nuser"]:

        #email = request.GET["user"]
        #usuarios = Miembro.objects.filter(email__exact=email)

        #contraseña = request.GET['pass']

        email = request.GET["nuser"]
        usuarios = Miembro.objects.filter(email__exact=email)

        contraseña = request.GET['new_pass']
        recontraseña = request.GET['re_pass']

        remensaje = 'Por favor, ingrese un correo registrado'

        for usuario in usuarios:

            if contraseña != recontraseña:
                renombre = usuario.nombre
                remensaje = "Contraseñas no coinciden"
                return render(request, "Portal.html", {"query": email, "remensaje": remensaje, "renombre": renombre})

            elif contraseña == "" or recontraseña == "":
                renombre = usuario.nombre
                remensaje = "Por favor, ingrese al menos 8 carácteres"
                return render(request, "Portal.html", {"query": email, "remensaje": remensaje, "renombre": renombre})

            else:
                renombre = usuario.nombre
                usuario.contraseña = recontraseña
                usuario.save()
                remensaje = "Estimad@",renombre,"su contraseña ha sido actualizada correctamente"
                return render(request, "Portal.html", {"query": email, "remensaje": remensaje, "renombre": renombre})




    else:
        remensaje = 'Por favor, no manosee el botón'

    return render(request, "Portal.html", { "remensaje": remensaje})

def calendario(request):
    return render(request, 'calendario.html', {})