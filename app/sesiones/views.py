# app/inscripciones/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Sesion, Alumno, Terapeuta, Curso

# Vista para listar todas las sesiones
def lista_sesiones(request):
    sesiones = Sesion.objects.all()  # Obtener todas las sesiones
    return render(request, 'inscripciones/lista_sesiones.html', {'sesiones': sesiones})

# Vista para obtener el detalle de una sesión específica
def detalle_sesion(request, id):
    sesion = get_object_or_404(Sesion, id_sesion=id)  # Buscar la sesión por ID
    return render(request, 'inscripciones/detalle_sesion.html', {'sesion': sesion})

# Vista para crear una nueva sesión
def crear_sesion(request):
    if request.method == 'POST':
        id_alumno = request.POST.get('id_alumno')
        id_curso = request.POST.get('id_curso')
        id_terapeuta = request.POST.get('id_terapeuta')
        fecha_sesion = request.POST.get('fecha_sesion')
        asistencia = request.POST.get('asistencia') == 'on'  # Si el checkbox está marcado
        observaciones = request.POST.get('observaciones')

        # Crear y guardar la nueva sesión
        sesion = Sesion(
            id_alumno=Alumno.objects.get(id_alumno=id_alumno),
            id_curso=Curso.objects.get(id_curso=id_curso),
            id_terapeuta=Terapeuta.objects.get(id_terapeuta=id_terapeuta),
            fecha_sesion=fecha_sesion,
            asistencia=asistencia,
            observaciones=observaciones
        )
        sesion.save()

        return redirect('lista_sesiones')  # Redirigir al listado de sesiones
    else:
        alumnos = Alumno.objects.all()  # Obtener todos los alumnos
        cursos = Curso.objects.all()  # Obtener todos los cursos
        terapeutas = Terapeuta.objects.all()  # Obtener todos los terapeutas
        return render(request, 'inscripciones/crear_sesion.html', {
            'alumnos': alumnos,
            'cursos': cursos,
            'terapeutas': terapeutas,
        })

# Vista para editar una sesión existente
def editar_sesion(request, id):
    sesion = get_object_or_404(Sesion, id_sesion=id)  # Buscar la sesión por ID

    if request.method == 'POST':
        # Actualizar los campos de la sesión
        sesion.id_alumno = Alumno.objects.get(id_alumno=request.POST.get('id_alumno'))
        sesion.id_curso = Curso.objects.get(id_curso=request.POST.get('id_curso'))
        sesion.id_terapeuta = Terapeuta.objects.get(id_terapeuta=request.POST.get('id_terapeuta'))
        sesion.fecha_sesion = request.POST.get('fecha_sesion')
        sesion.asistencia = request.POST.get('asistencia') == 'on'  # Si el checkbox está marcado
        sesion.observaciones = request.POST.get('observaciones')

        sesion.save()  # Guardar los cambios en la sesión

        return redirect('detalle_sesion', id=id)  # Redirigir al detalle de la sesión editada

    else:
        alumnos = Alumno.objects.all()
        cursos = Curso.objects.all()
        terapeutas = Terapeuta.objects.all()

        return render(request, 'inscripciones/editar_sesion.html', {
            'sesion': sesion,
            'alumnos': alumnos,
            'cursos': cursos,
            'terapeutas': terapeutas,
        })

# Vista para eliminar una sesión
def eliminar_sesion(request, id):
    sesion = get_object_or_404(Sesion, id_sesion=id)  # Buscar la sesión por ID
    if request.method == 'POST':
        sesion.delete()  # Eliminar la sesión
        return redirect('lista_sesiones')  # Redirigir al listado de sesiones
    return render(request, 'inscripciones/eliminar_sesion.html', {'sesion': sesion})
