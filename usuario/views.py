from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
# Esto es utilizado para manejar erros si no parese lo que busca la funcion
from django.shortcuts import get_object_or_404
from .models import ModeloUsuario
from .models import Producto
from .models import Carrusel
from .forms import ProductForm
from .forms import UsuarioRegistroForm
from .forms import UsuarioLoginForm


class UsuarioRegistro(View):
    def get(self, request):
        form = UsuarioRegistroForm()
        return render(request, 'registracion/registro.html', {'form': form})

    def post(self, request):
        form = UsuarioRegistroForm(request.POST, request.FILES)
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'registracion/registro.html', {'error': 'Las contraseñas no coinciden'})

        user = ModeloUsuario.objects.create_user(
            email=email, password1=password1)
        return redirect('cardprincipal')


class UsuarioLoginView(View):
    def get(self, request):
        return render(request, 'registracion/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('cardprincipal')
        else:
            return render(request, 'registracion/login.html', {'error': 'Email o contraseña inválidos'})


class inicio_view(View):
    def get(self, request):
        return render(request, 'pantallas_usuarios/cardprincipal.html')

class cabecera_view(View):
    def get(self, request):
        return render(request, 'cabesera.html')


class pie_view(View):
    def get(self, request):
        return render(request, 'pie.html')

# Pantallas de las caregorias

class cardhombres_view(View):
    def get(self, request):
        producto_hombre = Producto.objects.filter(categoria=1, activo=True)  # El 1 es el id de la categoria hombre
        producto_hombre_r = list(producto_hombre)[::-1]
        prueva = Producto.objects.order_by('-id_producto')[:3]
        return render(request, 'pantallas_usuarios/cardhombres.html', {'producto_hombre_r': producto_hombre_r, 'prueva':prueva})


class cardmujeres_view(View):
    def get(self, request):
        producto_mujeres = Producto.objects.filter(categoria=2, activo=True)  # el 2 es el id de la categoria mujer
        producto_mujeres_r = list(producto_mujeres)[::-1]
        prueva = Producto.objects.order_by('-id_producto')[:3]
        return render(request, 'pantallas_usuarios/cardmujeres.html', {'producto_mujeres_r': producto_mujeres_r, 'prueva':prueva})


class cardcosmeticos_view(View):
    def get(self, request):
        producto_cosmetico = Producto.objects.filter(categoria=4, activo=True)  # el 4 es el id de la categoria cosmetico
        producto_cosmetico_r = list(producto_cosmetico)[::-1]
        prueva = Producto.objects.order_by('-id_producto')[:3]
        return render(request, 'pantallas_usuarios/cardcosmeticos.html', {'producto_cosmetico_r': producto_cosmetico_r, 'prueva':prueva})


class cardhogar_view(View):
    def get(self, request):
        producto_hogar = Producto.objects.filter(categoria=5, activo=True) # El numero 5 es el id de la categoria hogar
        producto_hogar_r = list(producto_hogar)[::-1]
        prueva = Producto.objects.order_by('-id_producto')[:3]
        return render(request, 'pantallas_usuarios/cardhogar.html', {'producto_hogar_r': producto_hogar_r, 'prueva':prueva})


class cardniños_view(View):
    def get(self, request):
        producto_child = Producto.objects.filter(categoria=3, activo=True) # El numero 3 es el id de la categoria niños
        producto_child_r = list(producto_child)[::-1]
        prueva = Producto.objects.order_by('-id_producto')[:3]
        return render(request, 'pantallas_usuarios/cardniños.html', {'producto_child_r': producto_child_r, 'prueva':prueva})


class cardprincipal_view(View):
    def get(self, request):
        product = Producto.objects.filter(activo=True)
        producto_r = list(product)[::-1]
        prueva = Producto.objects.order_by('-id_producto')[:3]
        return render(request, 'pantallas_usuarios/cardprincipal.html', {'producto_r': producto_r, 'prueva':prueva})
        

class detallesProductos_view(View):
    def get(self, request, id_producto):
        detalles = Producto.objects.filter(id_producto=id_producto)
        return render(request, 'pantallas_usuarios/detallesProductos.html', {'detalles': detalles})
    
# Pantallas de las opciones de usuarios

class lista_megusta_view(View):
    def get(self, request):
        return render(request, 'pantallas_usuarios/lista_megusta.html')


class carrito_view(View):
    def get(self, request):
        return render(request, 'pantallas_usuarios/carrito.html')


class pantallaMensajes_view(View):
    def get(self, request):
        return render(request, 'pantallas_usuarios/pantallaMensajes.html')


class quienes_somos_view(View):
    def get(self, request):
        return render(request, 'pantallas_usuarios/quienes_somos.html')
    
class carrusel_view(View):
    def get(self, request):
        prueva = Producto.objects.order_by('-id_producto')[:3]
        return render(request, 'carrusel.html',{'prueva': prueva})
    
class Estado_pedivo_view(View):
    def get(self, request):
        return render(request, 'pantallas_usuarios/estado_pedidos.html')

# Parte del manegador de la pagina


class agregar_producto_view(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'manegador/agregar_producto.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')
        return render(request, 'manegador/agregar_producto.html', {'form': form})


class lista_producto_view(View):
    def get(self, reuqest):
        productos = Producto.objects.filter(activo=True)
        return render(reuqest, 'manegador/lista_producto.html', {'productos': productos})
