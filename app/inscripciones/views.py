# app/inscripciones/views.py
# app/inscripciones/views.py
from rest_framework import viewsets
from .models import Inscripcion
from .serializers import InscripcionSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Vistas basadas en funciones para la interfaz web
@login_required
def lista_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'inscripciones/lista.html', {'inscripciones': inscripciones})

@login_required
def detalle_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id_inscripcion=id)
    return render(request, 'inscripciones/detalle.html', {'inscripcion': inscripcion})

@login_required
def crear_inscripcion(request):
    if request.method == 'POST':
        id_alumno = request.POST['id_alumno']
        id_curso = request.POST['id_curso']
        id_colegio = request.POST['id_colegio']
        inscripcion = Inscripcion.objects.create(
            id_alumno=id_alumno,
            id_curso=id_curso,
            id_colegio=id_colegio
        )
        messages.success(request, 'Inscripción creada exitosamente')
        return redirect('lista_inscripciones')
    return render(request, 'inscripciones/crear.html')

@login_required
def editar_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id_inscripcion=id)
    if request.method == 'POST':
        inscripcion.id_alumno = request.POST['id_alumno']
        inscripcion.id_curso = request.POST['id_curso']
        inscripcion.id_colegio = request.POST['id_colegio']
        inscripcion.save()
        messages.success(request, 'Inscripción actualizada exitosamente')
        return redirect('lista_inscripciones')
    return render(request, 'inscripciones/editar.html', {'inscripcion': inscripcion})

@login_required
def eliminar_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id_inscripcion=id)
    inscripcion.delete()
    messages.success(request, 'Inscripción eliminada exitosamente')
    return redirect('lista_inscripciones')

# Vistas de la API
class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer