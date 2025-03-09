from django import forms
from .models import Sesion
from app.alumnos.models import Alumno
from app.terapeutas.models import Terapeuta
from app.cursos.models import Curso

class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = ['id_alumno', 'id_curso', 'id_terapeuta', 'fecha_sesion', 'asistencia', 'observaciones']
        widgets = {
            'fecha_sesion': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'observaciones': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'id_alumno': 'Alumno',
            'id_curso': 'Curso',
            'id_terapeuta': 'Terapeuta',
            'fecha_sesion': 'Fecha y hora',
            'asistencia': 'Asistencia',
            'observaciones': 'Observaciones'
        }
    
    def __init__(self, *args, **kwargs):
        super(SesionForm, self).__init__(*args, **kwargs)
        
        # Configurar los campos de selección
        self.fields['id_alumno'].queryset = Alumno.objects.all()
        self.fields['id_curso'].queryset = Curso.objects.all()
        self.fields['id_terapeuta'].queryset = Terapeuta.objects.all()
        
        # Convertir el formato de fecha para edición
        if self.instance.pk and self.instance.fecha_sesion:
            self.initial['fecha_sesion'] = self.instance.fecha_sesion.strftime('%Y-%m-%dT%H:%M')