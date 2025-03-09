from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['alumno_nombre', 'alumno_apellidos', 'alumno_fecha_nacimiento']
        widgets = {
            'alumno_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'alumno_apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'alumno_fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
