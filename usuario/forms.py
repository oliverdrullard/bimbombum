from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ModeloUsuario
from .models import Producto
from .models import DatosEnvio 




class UsuarioRegistroForm(UserCreationForm):


    class Meta:
        model = ModeloUsuario
        fields = [ 'email', 'password1', 'password2','nombre','direccion','formato_pago']

        widgets = {
            'email':forms.EmailInput(attrs={'class':'campo_informacion', 'placeholder':'Email'}),
            'nombre':forms.TextInput(attrs={'class':'campo_informacion', 'placeholder':'Nombre'}),
            'formato_pago':forms.TextInput(attrs={'class':'campo_informacion', 'placeholder':'Formato de pago'}),
            'direccion':forms.TextInput(attrs={'class':'campo_informacion', 'placeholder':'Direccion'}),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class':'campo_informacion',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'campo_informacion', 
            'placeholder': 'Confirmación de contraseña'
        })

class UsuarioLoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'campo_informacion', 'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'campo_informacion', 'placeholder': 'Contraseña'})
    )





class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = ['nombre', 'descripcion', 'colores', 'zise1', 'imagen', 'categoria', 'precio','stock','activo']

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control formcontrol campo_producto'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control descrip formcontrol campo_producto'}),
            'colores': forms.TextInput(attrs={'class':'form-control formcontrol campo_producto','placeholder':'Negro,Verde,Azul'}),
            'zise1': forms.TextInput(attrs={'class':'form-control formcontrol campo_producto','placeholder':'S,M,L'}),
            'imagen': forms.FileInput(attrs={'class':'form-control formcontrol campo_producto'}),
            'categoria': forms.Select(attrs={'class':'form-control formcontrol campo_producto'}),
            'precio': forms.NumberInput(attrs={'class':'form-control formcontrol campo_producto '}),
            'stock': forms.NumberInput(attrs={'class':'form-control formcontrol campo_producto '}),
            'activo': forms.CheckboxInput(attrs={'class':'sin_cls '}),
            
        }

class DatosEnviadosForm(forms.ModelForm):
    class Meta:
        model = DatosEnvio

        fields = ['nombre','telefo','provincia','sector','referencia','forma_pago']

        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-informacion', 'placeholder':'Nombre'}),
            'telefo':forms.TextInput(attrs={'class': 'form-informacion', 'placeholder':'Telefono'}),
            'provincia':forms.TextInput(attrs={'class': 'form-informacion', 'placeholder':'Povincia'}),
            'sector':forms.TextInput(attrs={'class': 'form-informacion', 'placeholder':'Sector'}),
            'referencia':forms.TextInput(attrs={'class': 'form-informacion', 'placeholder':'Referencia'}),
            'forma_pago':forms.RadioSelect(attrs={'class': 'forma-pago-opcion'}),
        }