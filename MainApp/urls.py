from django.urls import path
from .views import *

app_name = 'MainApp'

urlpatterns = [
    path("",                    Index.as_view(),            name = "index"),
    path("index",               Index.as_view(),            name = "index"),
    path("login",               Login.as_view(),            name = "login"),
    path("logout",              logout,                     name = "logout"),
    path("register",            Register.as_view(),         name = "register"),
    path("profile",             Profile.as_view(),          name = "profile"),
    path("cart",                Cart.as_view(),             name = "cart"),
    path("action",              action,                     name = "action"),
    path("adventures",          adventures,                 name = "adventures"),
    path("rpg",                 rpg,                        name = "rpg"),
    path("sports",              sports,                     name = "sports"),
    path("strategy",            strategy,                   name = "strategy"),
    path("api-chuck-norris",    APIChuckNorris.as_view(),   name = "api-chuck-norris"),
    path("api-random-user",     APIRandomUser.as_view(),    name = "api-random-user"),
    path("apis-internas",       APIsInternas.as_view(),     name = "apis-internas"),
    path("api-juegos",          api_juegos,                 name = "api-juegos"),
    path("api-categorias",      api_categorias,             name = "api-categorias"),
]