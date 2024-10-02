from .models import XE_Usuario, XE_Juego, XE_Categoria
from rest_framework import serializers

# Serializer de Usuario
# Para poder ocuparlo en el login
class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = XE_Usuario
        fields = '__all__'


# Serializer de Juego
class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = XE_Juego
        fields = '__all__'


# Serializer de Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = XE_Categoria
        fields = '__all__'




