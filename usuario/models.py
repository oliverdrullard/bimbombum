from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class ModeloUsuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100, default='')
    direccion = models.CharField(max_length=100, null=False, default='')
    formato_pago = models.CharField(max_length=100, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
  
class Puesto(models.Model):
    id_puesto = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)

    def __str__(self) :
        return self.nombre
    
class Sueldo(models.Model):
    id_sueldo = models.AutoField(primary_key= True)
    sueldo = models.DecimalField(max_digits=20,decimal_places=2)
    puesto = models.ForeignKey(Puesto,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.sueldo

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    

    def __str__(self):
        return self.nombre


class  Lista_usuario(models.Model):
    usuario_id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre
    

class  lista_megusta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto',on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)    

    class Meta:
        unique_together = ('usuario','producto') # Para evitar  duplicado

class Producto(models.Model):
    id_producto = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    zise1 = models.CharField(max_length=10)
    colores = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='static/')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,decimal_places=2, default='')
    stock = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key= True)
    numero_pedidos = models.IntegerField()
    estado = models.CharField(max_length=100,choices=[('Pendiente','Pendiente'),('Enviado','Enviado'),('Entragado','Entregado')])
    idusuario = models.ForeignKey(Lista_usuario,on_delete=models.CASCADE)
    idproducto = models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_pedidos

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    numero_factura = models.IntegerField()
    monto = models.DecimalField(max_digits=100,decimal_places=4)
    idpedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    # idlisataDeusuario = models.ForeignKey(Lista_usuario,on_delete=models.CASCADE)

class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length=200)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Empleado(models.Model):
    id_empledo = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length=200)
    puesto = models.ForeignKey(Puesto,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key= True)
    numero_venta = models.IntegerField()
    fecha = models.DateField()
    idfactura = models.ForeignKey(Factura,on_delete=models.CASCADE)
    idpedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.numero_venta
    
class Carrusel(models.Model):
    idproducto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='carrusel/')

# olivercontreras919@gmail.com, 123456789