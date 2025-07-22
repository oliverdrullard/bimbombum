from django.core.exceptions import PermissionDenied
def manegador(user):
    if not user.groups.filter(name='usuarioManager').exists():
        raise PermissionDenied  
    return True
def clientes(user):
    if not user.groups.filter(name='usuarioCliente').exists():
        raise PermissionDenied  
    return True
    # return user.is_authenticated and user.groups.filter(name ='usuarioManager').exists()