# app/inscripciones/views.py

from django.shortcuts import render

def lista_inscripciones(request):
    # Lógica para listar inscripciones
    return render(request, 'inscripciones/lista.html')  # Asegúrate de que la plantilla exista

def detalle_inscripcion(request, id):
    # Lógica para obtener el detalle de una inscripción específica
    return render(request, 'inscripciones/detalle.html', {'id': id})  # Asegúrate de que la plantilla exista

def crear_inscripcion(request):
    # Lógica para crear una nueva inscripción
    return render(request, 'inscripciones/crear.html')  # Asegúrate de que la plantilla exista

def editar_inscripcion(request, id):
    # Lógica para editar una inscripción existente
    return render(request, 'inscripciones/editar.html', {'id': id})  # Asegúrate de que la plantilla exista