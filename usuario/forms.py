from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ModeloUsuario
from .models import Producto
from .models import Usuario



class UsuarioRegistroForm(UserCreationForm):


    class Meta:
        model = ModeloUsuario
        fields = [ 'email', 'password1', 'password2','nombre','direccion','formato_pago']

        widgets = {
            'email':forms.EmailInput(attrs={'class':'campo_informacion', 'placeholder':'Email'}),
            'nombre':forms.TextInput(attrs={'class':'campo_informacion', 'placeholder':'Nombre'}),
            'formato_pago':forms.TextInput(attrs={'class':'campo_informacion', 'placeholder':'Formato de pago'}),
            'direccion':forms.TextInput(attrs={'class':'campo_informacion', 'placeholder':'Direccion'}),
            'password1':forms.PasswordInput(attrs={'class':'campo_informacion', 'placeholder':'Contraceña'}),
            'password2':forms.PasswordInput(attrs={'class':'campo_informacion', 'placeholder':'Confirmacion de contraceña'}),

        }


class UsuarioLoginForm(forms.Form):

    class Meta:
        model = ModeloUsuario

        fields = ['nombre', 'password1']

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'input-contenedor', 'placeholder':'Nombre'}),
            'password1':forms.PasswordInput(attrs={'class':'input-contenedor', 'placeholder':'Contraseña'})
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = ['nombre', 'descripcion', 'colores', 'imagen', 'categoria', 'precio','stock','activo']

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control formcontrol campo_producto'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control descrip formcontrol campo_producto'}),
            'colores': forms.TextInput(attrs={'class':'form-control formcontrol campo_producto'}),
            'imagen': forms.FileInput(attrs={'class':'form-control formcontrol campo_producto'}),
            'categoria': forms.Select(attrs={'class':'form-control formcontrol campo_producto'}),
            'precio': forms.NumberInput(attrs={'class':'form-control formcontrol campo_producto '}),
            'stock': forms.NumberInput(attrs={'class':'form-control formcontrol campo_producto '}),
            'activo': forms.CheckboxInput(attrs={'class':'sin_cls '}),
        }

