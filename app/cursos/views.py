# app/cursos/views.py

from django.shortcuts import render

def lista_cursos(request):
    # Lógica para listar cursos
    return render(request, 'cursos/lista.html')  # Asegúrate de que la plantilla exista

def detalle_curso(request, id):
    # Lógica para obtener el detalle de un curso específico
    return render(request, 'cursos/detalle.html', {'id': id})  # Asegúrate de que la plantilla exista

def crear_curso(request):
    # Lógica para crear un nuevo curso
    return render(request, 'cursos/crear.html')  # Asegúrate de que la plantilla exista

def editar_curso(request, id):
    # Lógica para editar un curso existente
    return render(request, 'cursos/editar.html', {'id': id})  # Asegúrate de que la plantilla exista