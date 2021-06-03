from django.db import models
from django.utils import timezone
    

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

opciones= [[0,"Hogar de cristo"],[1,"Cuaniquen"],[2,"Fundacion las rosas"],[3,"Fundacion luz"],[4,"Teleton"]]

class Miembro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_pat = models.CharField(max_length=15, null=True)
    apellido_mat = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    contraseña = models.CharField(max_length=15, null=True)
    cel = models.CharField(max_length=15)
    institucion = models.IntegerField(choices=opciones,max_length=15, null=True)
    photo = models.ImageField(upload_to = "perfil", null=True)
    pin = models.IntegerField(max_length=15, default=000)

    def __str__(self):

        return self.nombre

class Organizaciones(models.Model):
    nombre_organizacion= models.CharField(max_length=30, null=False)
    email_organizacion= models.EmailField()
    id_organizacion= models.IntegerField(max_length=10, null=False)
    descripcion_organizacion= models.CharField(max_length=200, null=True)

    def str(self):


        return self.nombre_organizacion


# Create your models here.
