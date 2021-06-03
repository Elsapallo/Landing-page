from django import forms
from .models import Miembro

class cambiarperfil(forms.ModelForm):

    class cliente:
        model = Miembro
        fields = ["nombre","apellido_pat","apellido_mat","email","contraseña","cel","institucion","photo"]
        