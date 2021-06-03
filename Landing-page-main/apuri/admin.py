from django.contrib import admin
from .models import Post, Miembro,Organizaciones

class funcionarios(admin.ModelAdmin):
    list_display = ["nombre","apellido_pat","apellido_mat"]
    search_fields = ["nombre"]
    list_per_page = 10

admin.site.register(Post)
admin.site.register(Miembro,funcionarios)
admin.site.register(Organizaciones)
# Register your models here.
