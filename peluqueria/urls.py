from django.contrib import admin
from django.urls import path
from django.shortcuts import render


#Views de la applications
from applications.views import lista_clientes, lista_empleados, lista_servicios, lista_turnos, coloracion,corte,tratamiento,home,restablecer
from applications.views import register, logout_request, login_request

###############

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', home, name='home'),

    # Login y Registro
    path('logout/', logout_request, name= 'logout'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('restablecer/', restablecer, name='restablecer'),
    


    # Apps
    path('empleados/', lista_empleados, name='lista_empleados'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('servicios/', lista_servicios, name='lista_servicios'),
    path('turnos/', lista_turnos, name='lista_turnos'),
    path('coloracion/',coloracion, name='coloracion'),
    path('corte/',corte, name='corte'),
    path('tratamiento/',tratamiento, name='tratamiento')
    
]