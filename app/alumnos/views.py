# app/alumnos/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Alumno

@login_required
def home(request):
    alumnos = Alumno.objects.all()
    return render(request, "gestionAlumnos.html", {"alumnos": alumnos})

@login_required
def registrarAlumno(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        apellidos = request.POST['txtApellidos']
        fecha_nacimiento = request.POST['txtFechaNacimiento'] or None
        
        alumno = Alumno.objects.create(
            alumno_nombre=nombre,
            alumno_apellidos=apellidos,
            alumno_fecha_nacimiento=fecha_nacimiento
        )
        messages.success(request, '¡Alumno registrado correctamente!')
        return redirect('/alumnos/')  # Redirect to absolute URL
    return redirect('/alumnos/')

@login_required
def edicionAlumno(request, id_alumno):
    alumno = Alumno.objects.get(id_alumno=id_alumno)
    return render(request, "edicion_alumno.html", {"alumno": alumno})

@login_required
def editarAlumno(request):
    if request.method == 'POST':
        id_alumno = request.POST['txtID']
        nombre = request.POST['txtNombre']
        apellidos = request.POST['txtApellidos']
        fecha_nacimiento = request.POST['txtFechaNacimiento'] or None
        
        alumno = Alumno.objects.get(id_alumno=id_alumno)
        alumno.alumno_nombre = nombre
        alumno.alumno_apellidos = apellidos
        alumno.alumno_fecha_nacimiento = fecha_nacimiento
        alumno.save()
        
        messages.success(request, '¡Alumno actualizado correctamente!')
        return redirect('/alumnos/')  # Redirect to absolute URL
    return redirect('/alumnos/')

@login_required
def eliminarAlumno(request, id_alumno):
    alumno = Alumno.objects.get(id_alumno=id_alumno)
    alumno.delete()
    messages.success(request, '¡Alumno eliminado correctamente!')
    return redirect('/alumnos/')  # Redirect to absolute URL