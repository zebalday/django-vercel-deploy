# Render imports
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.http import JsonResponse
# Auth imports
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from .models import XE_Usuario, XE_TipoUsuario, XE_Region
from .forms import UserForm
from .serializers import UserSerialzer
# Modules
import requests
# Modelos & Forms
from .models import XE_Juego, XE_Categoria
from .forms import JuegoForm, CategoriaForm
# Serializers
from .serializers import JuegoSerializer, CategoriaSerializer



# ========================================
#           VISTAS PRINCIPALES
# ========================================

# Index Class
class Index(TemplateView):

    template_name = 'index.html'
    form = None
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass


# Login Class
class Login(TemplateView):

    template_name = 'login.html'
    form = None
    
    def get(self, request):
        return render(request, self.template_name)


    def post(self, request):

        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']

        # Verificia usuario
        try:
            usuario = XE_Usuario.objects.get(email = email)
            
            # Verifica contraseña
            if not (password == usuario.password):
                messages.error(request, "Contraseña o correo incorrectos.")
                return redirect('MainApp:login')

            # Serializa usuario
            usuario = UserSerialzer(usuario)
            messages.success(request, "Sesión iniciada correctamente.")
            request.session['usuario'] = usuario.data
            
            # Retorna
            return redirect('MainApp:profile')

        # XE_Usuario no existe
        except XE_Usuario.DoesNotExist:
            messages.error(request, "Este correo no está registrado.")
            return redirect('MainApp:login')
     

# Cerrar sesion
def logout(request):
    request.session.flush()
    storage = messages.get_messages(request)
    storage.used = True
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('MainApp:login')


# Register Class
class Register(TemplateView):

    template_name = 'register.html'
    context = {'form' : UserForm}
    
    def get(self, request):
        
        return render(request, self.template_name, self.context)


    def post(self, request):
        
        data = UserForm(request.POST)

        if data.is_valid():
            tipo_usuario = data.cleaned_data['tipo_usuario']
            username = data.cleaned_data['username']
            password = data.cleaned_data['password']
            nombre = data.cleaned_data['nombre']
            email = data.cleaned_data['email']
            telefono = data.cleaned_data['telefono']
            region = data.cleaned_data['region']

            new_user = XE_Usuario(
                tipo_usuario = tipo_usuario,
                username = username,
                password = password,
                nombre = nombre,
                region = region,
                email = email,
                telefono = telefono
            )
            new_user.save()

            messages.success(request, "¡Gracias por registrarte!")
            return redirect('MainApp:login')
        
        else:
            messages.error(request, "Error en el registro.")
            #print(data.errors)
            return redirect('MainApp:register')


# Edit Profile Class
class Profile(TemplateView):
    template_name = 'profile.html'
    context = {}

    def get(self, request):

        usuario = request.session['usuario']
        obj_usuario = XE_Usuario.objects.get(email = usuario['email'])

        form = UserForm(initial={
            'tipo_usuario' : usuario['tipo_usuario'],
            'username' : usuario['username'],
            'password' : usuario['password'],
            'nombre' : usuario['nombre'],
            'telefono' : usuario['telefono'],
            'email' : usuario['email'],
            'region' : usuario['region'],
        })

        self.context['form'] = form
        self.context['usuario'] = obj_usuario

        return render(request, self.template_name, self.context )

    # ACTUALIZAR DATOS
    def post(self, request):
        
        try:
            # Obtener datos
            print(request.POST)
            email = request.POST['email']
            region = XE_Region.objects.get(id = int(request.POST['region']))
            tipo_usuario = XE_TipoUsuario.objects.get(id = int(request.POST['tipo_usuario']))

            # Actualizar datos
            usuario = XE_Usuario.objects.get(email = email)
            usuario.tipo_usuario = tipo_usuario
            usuario.username = request.POST['username']
            usuario.password = request.POST['password']
            usuario.nombre = request.POST['nombre']
            usuario.telefono = request.POST['telefono']
            usuario.region = region
            usuario.save()

            # Actualizar sesion
            usuario = XE_Usuario.objects.get(email = email)
            self.context['usuario'] = usuario
            usuario = UserSerialzer(usuario)
            request.session['usuario'] = usuario.data
        
            # Return
            messages.success(request, "Información actualizada correctamente.")
            return redirect('MainApp:profile')
        
        except Exception as ex:
            print(ex)
            messages.error(request, "Ha ocurrido algún error.")
            return redirect('MainApp:profile')


# ========================================
#                  APIS
# ========================================

# API Randon User Class
class APIRandomUser(TemplateView):
    
    template_name = "api-random-user.html"
    context = {}

    def get(self, request):
        # Obtener usuario random
        self.context['random_user'] = get_random_user()
        return render(request, self.template_name, self.context)
    
    def post():
        pass


def get_random_user():
    # Petición a api de random user
    response = requests.get(url = "https://randomuser.me/api/")
    response = response.json()['results'][0]
    return response


# API Random User Class
class APIChuckNorris(TemplateView):
    
    template_name = "api-chuck-norris.html"
    context = {}

    def get(self, request):
        # Obtener usuario random
        self.context['chuck_fact'] = get_norris_fact()
        return render(request, self.template_name, self.context)
    
    def post():
        pass


def get_norris_fact():
    # Petición a api de random user
    response = requests.get(url = "https://api.chucknorris.io/jokes/random")
    response = response.json()
    return response


# Apis Internas de Juegos y Categoría
class APIsInternas(TemplateView):

    template_name = "apis-internas.html"

    # Forms
    form_juego = JuegoForm()
    form_categoria = CategoriaForm()

    # Contexto
    context = {
        'form_juego' : form_juego,
        'form_categoria' : form_categoria
    }

    def get(self, request):

        # Datos
        list_juegos = XE_Juego.objects.all().order_by('-precio')[:5]
        list_categorias = XE_Categoria.objects.all().order_by('nombre')[:5]
        usuario = XE_Usuario.objects.get(email = request.session['usuario']['email'])
        self.context['list_juegos'] = list_juegos
        self.context['list_categorias'] = list_categorias
        self.context['usuario'] = usuario

        return render(request, self.template_name, self.context)

    def post(self, request):
        
        print(request.POST)

        try:
            if request.POST['tipo_form'] == 'categoria':
                new_categoria = XE_Categoria(nombre = request.POST['nombre'])
                new_categoria.save()
            
            else:
                data_juego = JuegoForm(request.POST)
                if data_juego.is_valid():
                    nombre = data_juego.cleaned_data['nombre']
                    categoria = data_juego.cleaned_data['categoria']
                    precio = data_juego.cleaned_data['precio']

                    XE_new_juego = XE_Juego(
                        nombre = nombre,
                        categoria = categoria,
                        precio = precio
                    ).save()

        except Exception as ex:
            raise
            #print(ex)
        
        return redirect('MainApp:apis-internas')


# Listar todos los juegos
def api_juegos(request):
    data = listado('juegos')
    return JsonResponse(data)


# Listar todas las categorias
def api_categorias(request):
    data = listado('categorias')
    return JsonResponse(data)


# Obtener data
def listado(tipo : str):
    
    match tipo:
        case 'juegos':
            juegos = XE_Juego.objects.all()
            listado = JuegoSerializer(juegos, many = True)
        case 'categorias':
            categorias = XE_Categoria.objects.all()
            listado = CategoriaSerializer(categorias, many = True)
    
    return {'listado' : listado.data}


# =====================================
#         VISTAS SECUNDARIAS
# =====================================

# Cart Class
class Cart(TemplateView):

    template_name = 'cart.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass

# Action view
def action(request):
    return render(request, 'action.html')

# Adventures view
def adventures(request):
    return render(request, 'adventures.html')

# RPG view
def rpg(request):
    return render(request, 'rpg.html')

# Sports view
def sports(request):
    return render(request, 'sports.html')

# Strategy view
def strategy(request):
    return render(request, 'strategy.html')