from django.db import models
from datetime import date


############
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField('email', unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)
    is_empleado = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']


    def get_full_name(self):
        full_name = '%s %s' % (self.nombre, self.apellido)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return f'{self.email}- {self.get_full_name()}'

######



class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dni = models.CharField(max_length=8, verbose_name='DNI', null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', default='2000-01-01')
    telefono = models.CharField(max_length=15, null=True, blank=True)
    domicilio = models.CharField('Domicilio', max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user} '


    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
    
class Servicios(models.Model):
    tipo_servicio = models.CharField('Nombre de Servicio', max_length=50, blank=True)
    costo = models.IntegerField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.tipo_servicio
    
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=8, verbose_name='DNI', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', default='2000-01-01')
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    domicilio = models.CharField('Domicilio', max_length=100, null=True, blank=True)
    
    puesto = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    def __str__(self):
        return f' {self.user} - {self.puesto} '

    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
    
class Turnos (models.Model):
    tipo_turno = models.CharField('Turno',max_length=100)
    nombre_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo_servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    costo = models.IntegerField()
    observaciones = models.CharField(max_length=100)
    fecha_hora = models.DateField()

    def __str__(self):
        return self.tipo_turno
    
    def __str__(self):
        return f' {self.nombre_cliente} - {self.nombre_empleado} - {self.tipo_servicio}'