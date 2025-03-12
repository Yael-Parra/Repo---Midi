# app/info_padres_tutores_legales/serializers.py
from rest_framework import serializers
from .models import InfoPadreTutor

class InfoPadreTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPadreTutor  # Especifica el modelo
        fields = '__all__'  # Incluye todos los campos del modelo