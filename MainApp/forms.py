from django import forms
from django.forms import ModelForm
from django.forms import Form
from .models import XE_Usuario, XE_TipoUsuario, XE_Region, XE_Juego, XE_Categoria
from phonenumber_field.modelfields import PhoneNumberField


# Formulario de usuario
class UserForm(ModelForm):

    class Meta:

        # OPCIONES DE REGION
        #regiones = XE_Region.objects.all()
        regiones = ['XE_Region.objects.all()']
        # OPCIONES DE USUARIO
        #tipos_usuario = XE_TipoUsuario.objects.all()
        
        tipos_usuario = [
            ("ADM", "ADMINISTRADOR"),
            ("VEN", "VENDEDOR"),
            ("CLI", "CLIENTE")
        ]

        model = XE_Usuario
        fields = [
            'tipo_usuario',
            'username',
            'password',
            'nombre',
            'email',
            'telefono',
            'region',
        ]
        widgets = {
            'tipo_usuario' : forms.Select(choices=tipos_usuario,
                                        attrs={
                                            'class':'form-input',
                                            'placeholder':'Tipo Usuario',
                                            'title':'Seleccione su tipo',
                                            'required':True
                                        }),
            'username' : forms.TextInput(attrs={'class':'form-input',
                                            'placeholder':'Username',
                                            'title':'Nombre de usuario'
                                            }),
            'password' : forms.PasswordInput(attrs={'class':'form-input',
                                            'pattern' : '^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&=?¡¿])[A-Za-z\d!#$%&=?¡¿]{6,25}$',
                                            'placeholder':'Contraseña',
                                            'title':'Contraseña'
                                            }),
            'nombre' : forms.TextInput(attrs={'class':'form-input',
                                            'placeholder':'Nombre',
                                            'title':'Ingrese su nombre'
                                            }),
            'email' : forms.EmailInput(attrs={'class':'form-input',
                                            'placeholder':'Email',
                                            'title':'Correo electrónico'
                                            }),
            'telefono' : forms.TextInput(attrs={'class':'form-input',
                                            'placeholder':'Teléfono (+569...)',
                                            'type': 'tel',
                                            'pattern': '^\+569\d{8}$',
                                            'maxlenght':'12',
                                            'title':'Número telefónico (+569XXXXXXXX)'
                                            }),
            'region' : forms.Select(choices=regiones,
                                        attrs={
                                            'class':'form-input',
                                            'placeholder':'Región',
                                            'title':'Seleccione su región',
                                            'required':True
                                        }),
        }
        labels = {
            'tipo_usuario' : 'Tipo usuario',
            'username' : 'Nombre de usuario',
            'password' : 'Contraseña',
            'name' : 'Nombre',
            'email' : 'Correo',
            'telefono' : 'Teléfono',
            'region' : 'Región'
        }


# Formulario de juegos para API
class JuegoForm(ModelForm):
    class Meta:
        model = XE_Juego
        fields = [
            'categoria',
            'nombre',
            'precio'
        ]
        widgets = {
            'categoria' : forms.Select(attrs = {'class':'form-input',
                                            'title':'Seleccione categoría',
                                            'required':True}),
            'nombre' : forms.TextInput(attrs = {'class':'form-input',
                                            'placeholder':'Nombre del Juego',
                                            'title':'Nombre categoría'
                                            }),
            'precio' : forms.NumberInput(attrs={
                                                'class': 'form-input',
                                                'min': '1',
                                                'step': '1',
                                            })
        }
        labels = {
            'categoria': 'Categoría',
            'nombre': 'Nombre de juego',
            'precio': 'Precio unitario'
        }


# Formulario de categorias para API
class CategoriaForm(ModelForm):
    class Meta:
        model = XE_Categoria
        fields = [
            'nombre',
        ]
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-input',
                                            'placeholder':'Nombre categoría',
                                            'title':'Nombre categoría'
                                            }),
        }
        labels = {
            'nombre': 'Nombre categoría',
        }