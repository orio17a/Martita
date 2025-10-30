from django.shortcuts import render


#---------------------------------- LOGIN y demas en uso ----------------------------------
#from del registro
from .forms import CustomUserCreationForm 
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

##para poner mensajes
from django.contrib import messages

##############################################################################
from .models import Cliente, Empleado, Servicios, Turnos

from django.shortcuts import render, redirect # <-- Añadir redirect aquí
from django.http import JsonResponse # <-- ¡ESTO ES CLAVE!
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})

def lista_servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios/servicios.html', {'servicios': servicios})

def lista_turnos(request):
    turnos = Turnos.objects.all()
    return render(request, 'turnos/turnos.html', {'turnos': turnos})

def coloracion (request):
    return render(request, 'coloracion/coloracion.html')

def corte (request):
    return render(request, 'corte/corte.html')

def tratamiento (request):
    return render(request, 'tratamiento/tratamiento.html')

def home(request):
    return render(request, "index/index.html")

def restablecer (request):
    return render(request, "login/login_restablecer.html")

##############################################################################


#---------------------------------- LOGIN y demas en uso ----------------------------------

##Registro Usuario

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            
            # 1. ESTABLECER EL MENSAJE DE BIENVENIDA CON EL NOMBRE
            messages.success(request, f'Bienvenido {nombre_usuario}, tu cuenta fue creada exitosamente!')
            
            # 2. INICIAR SESIÓN AUTOMÁTICAMENTE
            login(request, usuario)
            
            # 3. REDIRECCIONAR A HOME (Donde se verá el mensaje)
            return redirect('home') 
        else:
            # En caso de error, muestra los mensajes en la misma página de registro
            for field, errors in form.errors.items():
                # Mostrar el primer error de cada campo
                messages.error(request, f'{field.capitalize()}: {errors.as_text()}') 

    form = CustomUserCreationForm()
    return render(request, 'registro/registro.html', {"form": form})


##para cerrar sesion
def logout_request(request):
    logout(request)
    messages.info(request, "Has cerrado sesion exitosamente")
    return redirect('home')


##para iniciar sesion
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=nombre_usuario, password=contrasena)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {nombre_usuario}')
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contrasena incorrecta')
        else:
            messages.error(request, 'Usuario o contrasena incorrecta')
    
    form = AuthenticationForm() #esto es para que aparezca el formulario vacio
    return render(request, 'login/Login.html', {'form':form})

#---------------------------------- LOGIN y demas en uso ----------------------------------