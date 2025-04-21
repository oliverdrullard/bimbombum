from .models import Categoria
from .models import Producto
from django.db.models import Q

def categorias_disponibles(request):
    categorias = Categoria.objects.filter(activo=True)
    return{'categorias':categorias}

def barra_busqueda_context(request):
    query = request.GET.get('buscar', '').strip()
    productos_resultado = []

    if query:
        productos_resultado = Producto.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(zise1__icontains=query) |
            Q(colores__icontains=query) |
            Q(precio__icontains=query)
        ).distinct().order_by('-id_producto')  # ordena del más nuevo al más viejo
    print(productos_resultado)
    return {
        'buscar_query': query,
        'resultados_busqueda': productos_resultado
    }
    