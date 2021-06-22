from django.db import models

from django.contrib.auth.models import BaseUserManager 

class UserManager(BaseUserManager, models.Manager):
        #funcion privada general con todos los atributos para usuarios y superusuarios
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):#va a heredar los campos del modelo "users"
        user = self.model( #aqui los parametros deben ser los que contempla el modelo "users"
            username=username,
            email=email,
            is_staff=is_staff, #por heredar del modelo users, que a su vez hereda de AbstractBaseUser se puede declarar este atributo
            is_superuser=is_superuser,#por heredar del modelo users, que a su vez hereda de AbstractBaseUser se puede declarar este atributo
            **extra_fields #este atributo permite crear otros campos 
        )
        user.set_password(password)# esta función viene en el AbstracBaseUser (importado en el models) y se usa para crear el password, el cual se encripta
        user.save(using=self.db)#almacena el psswd en la db
        return user
    
    #funcion para crear usuarios normales
    def create_user(self, username, email, password=None, **extra_fields):#solo declaro como argumentos los campos obligatorios al crear un usuario normal.
        return self._create_user(username, email, password, False, False, **extra_fields) #llama la función privada para crear el usuario normal
        #Se le pasa como parametro al return False, False para desactivar is_staff y is_superuser para que no sea un superusuario

    #función para crear supersusurio
    def create_superuser(self, username, email, password=None,**extra_fields ):
        return self._create_user(username, email, password, True, True, **extra_fields)#True, True es el valor de los atributos booleanos is_staff e is_superuser y su valor es True.


#is_staff es un atributo booleano inidca "si puede acceder al administrador"
#is_superuser es un atributo booleano inidca "si es o no un superusuario"