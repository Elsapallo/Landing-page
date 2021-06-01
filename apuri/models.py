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


class Miembro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_pat = models.CharField(max_length=15, null=True)
    apellido_mat = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    contraseña = models.CharField(max_length=15, null=True)
    cel = models.CharField(max_length=15)
    institucion = models.CharField(max_length=50, null=True) #default = "invitado"
    pin = models.IntegerField(max_length=15, default=00000)

    def __str__(self):

        return self.nombre


