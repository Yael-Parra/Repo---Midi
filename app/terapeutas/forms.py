# forms.py
from django import forms
from .models import Terapeuta

class TerapeutaForm(forms.ModelForm):
    class Meta:
        model = Terapeuta
        fields = [
            'terapeuta_nombre',
            'terapeuta_apellidos',
            'terapeuta_cedula',
            'terapeuta_telefono',
            'terapeuta_email',
        ]
        widgets = {
            'terapeuta_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'terapeuta_apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'terapeuta_cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'terapeuta_telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'terapeuta_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }