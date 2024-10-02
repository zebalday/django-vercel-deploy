from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


# TIPO USUARIO
class XE_TipoUsuario(models.Model):
    descripcion = models.TextField(
        max_length = 50,
        verbose_name = 'Tipo usuario',
        blank = False,
        null = False,
        unique = False
    )

    def __str__(self):
        return (f"{self.descripcion}")


# REGION
class XE_Region(models.Model):
    nombre = models.CharField(
        max_length = 100,
        verbose_name = "Región",
        blank = False,
        null = False,
    )

    def __str__(self):
        return (f"{self.nombre}")


# USUARIO
class XE_Usuario(models.Model):
    nombre = models.TextField(
        max_length = 150,
        verbose_name = "Nombre",
        blank = False,
        null = False,
        editable = True
    )
    username = models.TextField(
        max_length = 150,
        verbose_name = "Nombre de usuario",
        blank = False,
        null = False,
        unique = False,
        editable = True
    )
    password = models.TextField(
        max_length = 150,
        verbose_name = "Contraseña",
        blank = False,
        null = False,
        unique = False,
        editable = True
    )
    email = models.EmailField(
        max_length = 250,
        verbose_name = "Correo",
        blank = False,
        null = False,
        unique = True,
        editable = True
    )
    tipo_usuario = models.ForeignKey(
        XE_TipoUsuario,
        on_delete = models.CASCADE,
        verbose_name = 'Tipo',
        editable = True,
        blank = False,
        null = False
    )
    region = models.ForeignKey(
        XE_Region,
        on_delete = models.CASCADE,
        verbose_name = 'Región',
        editable = True,
        blank = False,
        null = False
    )
    telefono = PhoneNumberField(
        region = "CL",
        verbose_name = "Teléfono",
        blank = False,
        null = False,
        unique = False,
        editable = True
    )

    def __str__(self):
        return (f"{self.username}")


# ===============================================
#           MODELOS PARA APIS
# ===============================================


# CATEGORIA JUEGO
class XE_Categoria(models.Model):
    nombre = models.TextField(
        max_length = 50,
        verbose_name = 'Categoría Juego',
        blank = False,
        null = False,
        unique = False
    )

    def __str__(self):
        return (f"{self.nombre}")


# JUEGO
class XE_Juego(models.Model):
    categoria = models.ForeignKey(
        XE_Categoria,
        on_delete = models.CASCADE,
        editable = True,
        blank = False,
        null = False
    )
    nombre = models.TextField(
        max_length = 50,
        verbose_name = 'Tipo usuario',
        blank = False,
        null = False,
        unique = False
    )
    precio =  models.IntegerField(
        editable = True,
        validators = [MinValueValidator(0)],
        verbose_name = 'Precio',
        blank = False,
        null = False
    )

    def __str__(self):
        return (f"{self.nombre}")