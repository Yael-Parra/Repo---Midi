from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['id_colegio', 'nombre_curso']
        widgets = {
            'id_colegio': forms.Select(attrs={'class': 'form-control'}),
            'nombre_curso': forms.TextInput(attrs={'class': 'form-control'})
        }