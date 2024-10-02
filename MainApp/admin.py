from django.contrib import admin
from .models import *


class AdminRegion(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

class AdminTipoUsuario(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)
    ordering = ('descripcion',)

class AdminUsuario(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)
    ordering = ('username',)


# Register your models here.
admin.site.register(XE_Region, AdminRegion)
admin.site.register(XE_TipoUsuario, AdminTipoUsuario)
admin.site.register(XE_Usuario, AdminUsuario)
    