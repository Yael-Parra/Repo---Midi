from django.shortcuts import render
from .models import Curso

def home(request):
    cursoslistados = Curso.objects.all()
    return render(request, 'academico/gestion_cursos.html', {'cursos': cursoslistados})
    
