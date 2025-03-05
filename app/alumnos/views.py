# app/alumnos/views.py

from django.shortcuts import render

def index(request):
    # Lógica para la vista principal de alumnos
    return render(request, 'alumnos/index.html')  # Asegúrate de que la plantilla exista

def detalle(request, id):
    # Lógica para obtener el detalle de un alumno específico
    return render(request, 'alumnos/detalle.html', {'id': id})  # Asegúrate de que la plantilla exista

def crear_alumno(request):
    # Lógica para crear un nuevo alumno
    return render(request, 'alumnos/crear.html')  # Asegúrate de que la plantilla exista

def editar_alumno(request, id):
    # Lógica para editar un alumno existente
    return render(request, 'alumnos/editar.html', {'id': id})  # Asegúrate de que la plantilla exista