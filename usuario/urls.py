from django.urls import path
from . import views

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

    
]