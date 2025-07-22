from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [

    path('categoria/<int:categoria_id>/',views.CategoriaView.as_view(), name='categoria'),
    path('registro/',views.UsuarioRegistro.as_view(),name='registro'),
    path('login/',views.UsuarioLoginView.as_view(),name='login'),
    path('logout/',views.UsuarioLogout.as_view(),name='logout'),
    path('cardprincipal/', views.cardprincipal_view.as_view(), name='cardprincipal'),
    path('lista_megusta/', views.lista_megusta_view.as_view(), name='lista_megusta'),
    path('carrito/', views.carrito_view.as_view(), name='carrito'),
    path('pantallaMensajes/', views.pantallaMensajes_view.as_view(), name='pantallaMensajes'),
    path('quienes_somos/', views.quienes_somos_view.as_view(), name='quienes_somos'),
    path('agregar_producto/', views.agregar_producto_view.as_view(), name='agregar_producto'),
    path('lista_producto/', views.lista_producto_view.as_view(), name='lista_producto'),
    path('estado_pedidos/', views.Estado_pedivo_view.as_view(), name='estado_pedidos'),
    path('detallesProductos/<id_producto>/', views.detallesProductos_view.as_view(), name='detallesProductos'),
    path('buscar/', views.ResultadosBusquedaView.as_view(), name='resultado_busqueda'),
    path('agregar_a_lista_me_gusta/<int:producto_id>/', views.agregar_a_lista_megusta.as_view(), name='agregar_a_lista_me_gusta'),
    path('eliminar_producto_lista_megusta/<int:producto_id>/', views.eliminar_producto_lista_megusta.as_view(), name='eliminar_producto_lista_megusta'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('Confirmar_pedido/', views.Confirmar_pedido.as_view(), name='Confirmar_pedido'),
    path('index/', views.index.as_view(), name='index'),

    
]