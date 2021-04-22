from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager#para conectar el manager con modelo primero debemos importarlo aqui en models

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin): #AbstractBaseUser por defecto contempla is_staff e is_superuser

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True) #blank=True este atributo no es obligatorio
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    #atributo booleano para que el usuario creado pueda acceder al administrador
    is_staff = models.BooleanField(default=False) #un usuario normal no puede acceder al admin, porque por defecto el campo o atributo is_staff esta en False
                                                  #aunque desde el superusuario al ingresar en la app users en el admin, e ingresar en un usuario, este tiene campo is_staff pero desactivado, y tildando desde superuser, se le pueden dar pleno acceso al admin.
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager() #conecta el manager con el modelo

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos