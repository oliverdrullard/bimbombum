from .models import Categoria

def categorias_disponibles(request):
    categorias = Categoria.objects.filter(activo=True)
    return{'categorias':categorias}