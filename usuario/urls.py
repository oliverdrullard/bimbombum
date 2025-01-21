from django.urls import path
from . import views

urlpatterns = [

    path('registro/',views.UsuarioRegistro.as_view(),name='registro'),
    path('login/',views.UsuarioLoginView.as_view(),name='login'),
    path('logout/',views.UsuarioLogout.as_view(),name='logout'),
    path('index/', views.inicio_view.as_view(), name='index'),
    path('cabecera/', views.cabecera_view.as_view(), name='cabecera'),
    path('pie/', views.pie_view.as_view(), name='pie'),
    path('cardhombres/', views.cardhombres_view.as_view(), name='cardhombres'),
    path('cardmujeres/', views.cardmujeres_view.as_view(), name='cardmujeres'),
    path('cardcosmeticos/', views.cardcosmeticos_view.as_view(), name='cardcosmeticos'),
    path('cardhogar/', views.cardhogar_view.as_view(), name='cardhogar'),
    path('carrusel/', views.carrusel_view.as_view(), name='carrusel'),
    path('cardprincipal/', views.cardprincipal_view.as_view(), name='cardprincipal'),
    path('cardniños/', views.cardniños_view.as_view(), name='cardniños'),
    path('lista_megusta/', views.lista_megusta_view.as_view(), name='lista_megusta'),
    path('carrito/', views.carrito_view.as_view(), name='carrito'),
    path('pantallaMensajes/', views.pantallaMensajes_view.as_view(), name='pantallaMensajes'),
    path('quienes_somos/', views.quienes_somos_view.as_view(), name='quienes_somos'),
    path('agregar_producto/', views.agregar_producto_view.as_view(), name='agregar_producto'),
    path('lista_producto/', views.lista_producto_view.as_view(), name='lista_producto'),
    path('estado_pedidos/', views.Estado_pedivo_view.as_view(), name='estado_pedidos'),
    path('detallesProductos/<id_producto>/', views.detallesProductos_view.as_view(), name='detallesProductos'),

    
]