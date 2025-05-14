from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Esto es utilizado para manejar erros si no parese lo que busca la funcion
from django.shortcuts import get_object_or_404
from .models import ModeloUsuario
from .models import Producto
from .models import Carrusel
from .forms import ProductForm
from .forms import UsuarioRegistroForm
from .forms import UsuarioLoginForm
from .models import Categoria
from .models import lista_megusta
from .carrito import Cart

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
                return redirect('cart:cardprincipal')
            else:
                return render(request, 'registracion/login.html', {'error': 'Email o contraseña inválidos'})
        return render(request, 'registracion/login.html', {'form': form, 'error': 'Datos inválidos'})
        
# para deslogear el usuario
class UsuarioLogout(View):
    def get(self, request):
        logout(request)
        return redirect('cart:cardprincipal')


# Pantallas de las caregorias

class CategoriaView(TemplateView):
    template_name = 'pantallas_usuarios/categoria.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.kwargs.get('categoria_id')
        categoria = Categoria.objects.get(id=categoria_id)
        productos = Producto.objects.filter(categoria=categoria, activo=True)
        productos = list(reversed(productos))
        carrusel = Producto.objects.filter(categoria=categoria, activo=True)[:3]

        context['producto_r'] = productos  
        context['categoria'] = categoria
        context['carrusel'] = carrusel
        return context

    
class cardprincipal_view(View):
    def get(self, request):
        product = Producto.objects.filter(activo=True)
        producto_r = list(product)[::-1]
        carrusel = Producto.objects.order_by('-id_producto')[:3]
        return render(request, 'pantallas_usuarios/cardprincipal.html', {'producto_r': producto_r, 'carrusel':carrusel,})
          
class detallesProductos_view(View):
    def get(self, request, id_producto):
        detalles = Producto.objects.filter(id_producto=id_producto)
        return render(request, 'pantallas_usuarios/detallesProductos.html', {'detalles': detalles})
    
# Pantallas de las opciones de usuarios
class ResultadosBusquedaView(TemplateView):
    template_name = 'pantallas_usuarios/resultado_busqueda.html'
    


class lista_megusta_view(LoginRequiredMixin, View):
   login_url = 'cart:login'
   def get(self, request):
        lista_me_gusta = lista_megusta.objects.filter(usuario=request.user)
        productos = [item.producto for item in lista_me_gusta]
        
        return render(request, 'pantallas_usuarios/lista_megusta.html', {'productos': productos})

class agregar_a_lista_megusta(LoginRequiredMixin, View):
    login_url = 'cart:login'
    def post(self, request, producto_id):
        producto = Producto.objects.get(id_producto=producto_id)

        if not lista_megusta.objects.filter(usuario=request.user, producto=producto).exists():
            lista_megusta.objects.create(usuario=request.user, producto=producto)
        
        return redirect('cart:lista_megusta')

class eliminar_producto_lista_megusta(LoginRequiredMixin, View):
    def post(self, request, producto_id):
        favorito = lista_megusta.objects.get(usuario=request.user,producto_id=producto_id)
        favorito.delete()

        return redirect('cart:lista_megusta')

class carrito_view(View):
    def get(self, request):
        return render(request, 'pantallas_usuarios/carrito.html')
    
def agregar_al_carrito(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id_producto=producto_id)

    cantidad_solicitada = int(request.POST.get('cantidad', 1))
    action = request.POST.get('action')

    # Obtenemos la cantidad actual del producto en el carrito
    cantidad_actual = cart.get_cantidad(producto)

    if action == 'increment':
        nueva_cantidad = cantidad_actual + 1
        if nueva_cantidad <= producto.stock:
            cart.add(producto=producto, cantidad=1)
    elif action == 'decrement':
        nueva_cantidad = cantidad_actual - 1
        if nueva_cantidad >= 1:
            cart.add(producto=producto, cantidad=-1)
    else:
        if cantidad_solicitada <= producto.stock:
            cart.add(producto=producto, cantidad=cantidad_solicitada)

    return redirect('cart:ver_carrito')

def eliminar_del_carrito(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id_producto=producto_id)
    cart.remove(producto)
    return redirect('cart:ver_carrito')

def ver_carrito(request):
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

class Confirmar_pedido(View):
    def get(self, request):
        return render(request, 'pantallas_usuarios/confipedido.html')

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
    def get(self, request):
        productos = Producto.objects.filter(activo=True)
        return render(request, 'manegador/lista_producto.html', {'productos': productos})
