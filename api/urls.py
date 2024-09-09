from django.urls import path
from . import views


urlpatterns = [
    # USUARIOS
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('users/', views.users_list, name='users'),
    path('users/delete/<int:id>/', views.users_delete, name='users_delete'),
    # GESTION LABORATORIO
    path('laboratorio/', views.laboratorio, name='laboratorio'),
    path('muestras/', views.muestras, name='muestras'),
    path('registerMuestra/', views.register_muestra, name='register_muestra'),
    path('registerCuTFeZn/', views.register_CutFeZn, name='register_CutFeZn'),
    path('CuTFeZn/', views.CutFeZn, name='CutFeZn'),
    path('CuS4FeS4MoS4/', views.CuS4FeS4MoS4, name='CuS4FeS4MoS4'),
    path('registerCuS4FeS4MoS4/', views.register_CuS4FeS4MoS4, name='register_CuS4FeS4MoS4'),
    path('registerMulti/', views.register_Multi, name='register_Multi'),
    path('Multi/', views.Multi, name='multi'),
]
