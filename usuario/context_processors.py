from .models import Categoria
from .models import Producto
from django.db.models import Q

def categorias_disponibles(request):
    categorias = Categoria.objects.filter(activo=True)
    return{'categorias':categorias}

# def buscardor(request):
#     producto_r = []
#     busqueda = request.GET.get('buscar')
#     busqueda_actual = busqueda

#     if busqueda:
#         producto_r = Producto.objects.filter(
#             Q(nombre__icontains=busqueda) |
#             Q(descripcion__icontains=busqueda) |
#             Q(zise1__icontains=busqueda) |
#             Q(colores__icontains=busqueda) |
#             Q(precio__icontains=str(busqueda))
#         ).distinct()

#     return {
#         'producto_r': producto_r,
#         'busqueda_actual': busqueda_actual
#     }
    