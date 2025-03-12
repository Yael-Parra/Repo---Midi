from rest_framework import serializers
from .models import Terapeuta

class TerapeutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terapeuta  # Especifica el modelo
        fields = '__all__'  # Incluye todos los campos del modelo