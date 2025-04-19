from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q 
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
# Esto es utilizado para manejar erros si no parese lo que busca la funcion
from django.shortcuts import get_object_or_404
from .models import ModeloUsuario
from .models import Producto
from .models import Carrusel
from .forms import ProductForm
from .forms import UsuarioRegistroForm
from .forms import UsuarioLoginForm
from .models import Categoria

# registro de usuarios
class UsuarioRegistro(View):

    @method_decorator(csrf_protect)
    def get(self, request):
        form = UsuarioRegistroForm()
        return render(request, 'registracion/registro.html', {'form': form})

    @method_decorator(csrf_protect)
    def post(self, request):
        form = UsuarioRegistroForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'registracion/registro.html', {'form': form})
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                return render(request, 'registracion/registro.html', {'form': form, 'error': 'Las contraseñas no coinciden'})

            user = ModeloUsuario.objects.create_user(
                email=form.cleaned_data['email'],
                password=password1,
                nombre=form.cleaned_data['nombre'],
                direccion=form.cleaned_data['direccion'],
                formato_pago=form.cleaned_data['formato_pago']
            )  
            return redirect('cardprincipal')
        return render(request, 'registracion/registro.html', {'form': form, 'error': 'Datos inválidos'})

# login del usuario 
class UsuarioLoginView(View):
    def get(self, request):
        form = UsuarioLoginForm()
        return render(request, 'registracion/login.html', {'form':form})

    def post(self, request):
        form = UsuarioLoginForm(request.POST)
        if not form.is_valid():
            print()
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('cardprincipal')
            else:
                return render(request, 'registracion/login.html', {'error': 'Email o contraseña inválidos'})
        return render(request, 'registracion/login.html', {'form': form, 'error': 'Datos inválidos'})
        
# para deslogear el usuario
class UsuarioLogout(View):
    def get(self, request):
        logout(request)
        return redirect('cardprincipal')


# Pantallas de las caregorias

class CategoriaView(TemplateView):
    template_name = 'pantallas_usuarios/categoria.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.kwargs.get('categoria_id')
        
        busqueda = self.request.GET.get('buscar')
        
        categoria = Categoria.objects.get(id=categoria_id)
        productos = Producto.objects.filter(categoria=categoria, activo=True)

        if busqueda:
            productos = Producto.objects.filter(
                Q(nombre__icontains = busqueda) |
                Q(descripcion__icontains = busqueda)|
                Q(zise1__icontains = busqueda)|
                Q(colores__icontains = busqueda)|
                Q(precio__icontains = str(busqueda))
            ).distinct()

        productos = list(reversed(productos))
        carrusel = Producto.objects.order_by('-id_producto')[:3]

        context['producto_r'] = productos  
        context['categoria'] = categoria
        context['carrusel'] = carrusel
        return context

    
class cardprincipal_view(View):
    def get(self, request):
        busqueda = request.GET.get('buscar')

        product = Producto.objects.filter(activo=True)

        if busqueda:
            product = Producto.objects.filter(
                Q(nombre__icontains = busqueda) |
                Q(descripcion__icontains = busqueda)|
                Q(zise1__icontains = busqueda)|
                Q(colores__icontains = busqueda)|
                Q(precio__icontains = str(busqueda))
            ).distinct()

        producto_r = list(product)[::-1]
        carrusel = Producto.objects.order_by('-id_producto')[:3]
        return render(request, 'pantallas_usuarios/cardprincipal.html', {'producto_r': producto_r, 'carrusel':carrusel,})
          
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
