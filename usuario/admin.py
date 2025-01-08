from django.contrib import admin

# Register your models here.

from .models import Categoria
from .models import Sueldo
from .models import Lista_usuario
from .models import Producto
from .models import Pedido
from .models import Factura
from .models import Proveedores
from .models import Empleado
from .models import Ventas
from .models import Puesto
from .models import Carrusel



admin.site.register(Categoria)
admin.site.register(Sueldo)
admin.site.register(Lista_usuario)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(Proveedores)
admin.site.register(Empleado)
admin.site.register(Ventas)
admin.site.register(Puesto)
admin.site.register(Carrusel)