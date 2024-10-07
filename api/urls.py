from django.urls import path
from . import views


urlpatterns = [
    # USUARIOS
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('users/', views.users_list, name='users'),
    path('users/delete/<int:id>/', views.users_delete, name='users_delete'),
    
    # CLIENTE
    path('clientes/', views.clientes_list, name='clientes'),
    path('registerCliente/', views.register_cliente, name='register_cliente'),
    
    # PROYECTOS
    path('proyectos/', views.proyectos_list, name='proyectos'),
    path('registerProyectos/', views.register_proyectos, name='register_proyectos'),
    
    # GESTION LABORATORIO
    path('laboratorio/', views.laboratorio, name='laboratorio'),
    path('muestras/', views.muestras, name='muestras'),
    path('registerMuestra/', views.register_muestra, name='register_muestra'),
    path('CuTFeZn/', views.CutFeZn, name='CutFeZn'),
    path('registerCuTFeZn/', views.register_CutFeZn, name='register_CutFeZn'),
    path('CuS4FeS4MoS4/', views.CuS4FeS4MoS4, name='CuS4FeS4MoS4'),
    path('registerCuS4FeS4MoS4/', views.register_CuS4FeS4MoS4, name='register_CuS4FeS4MoS4'),
    path('Multi/', views.Multi, name='multi'),
    path('registerMulti/', views.register_Multi, name='register_Multi'),
    
    # ODT
    path('registerODT/', views.register_ODT, name='registerODT'),
    path('ODT/', views.get_ODT, name='get_ODT'),
    path('ODTDetails/<str:id>/', views.get_ODTDetails, name='get_ODTDetails'),
   
   # TRABAJO
    path('registerElement/', views.register_ElementoMetodo, name='registerElement'),
    path('element/', views.get_elementos, name='get_ElementoMetodo'),
    path('registerMethod/', views.register_metodo, name='registerMethod'),
    path('method/', views.get_method, name='method'),
]
