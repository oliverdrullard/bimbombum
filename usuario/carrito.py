from decimal import Decimal
from django.conf import settings
from .models import Producto

class Cart:
    def __init__(self,request):
        self.session  = request.session # Guardando la seccion actual del usuario
        cart = self.session.get(settings.CART_SESSION_ID) #
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self,producto,cantidad=1,override_cantidad=False):
        producto_id = str(producto.id_producto)
        if producto_id not in self.cart:
            self.cart[producto_id] = {'cantidad': 0, 'precio': str(producto.precio)}
        if override_cantidad:
            self.cart[producto_id]['cantidad'] = cantidad
        else:
            self.cart[producto_id]['cantidad'] += cantidad
            
        if self.cart[producto_id]['cantidad'] <= 0:
            del self.cart[producto_id]
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.id_producto)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def get_cantidad(self, producto):
        producto_id = str(producto.id_producto)
        if producto_id in self.cart:
            return self.cart[producto_id]['cantidad']
        return 0
    
    def __iter__(self):
        producto_ids = self.cart.keys()
        productos = Producto.objects.filter(id_producto__in=producto_ids)

        for producto in productos:
            self.cart[str(producto.id_producto)]['producto'] = producto

        for item in self.cart.values():
            item['precio'] = Decimal(item['precio'])
            item['total'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()