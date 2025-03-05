# app/colegios/views.py

from django.shortcuts import render

def lista_colegios(request):
    # Lógica para listar colegios
    return render(request, 'colegios/lista.html')  # Asegúrate de que la plantilla exista

def detalle_colegio(request, id):
    # Lógica para obtener el detalle de un colegio específico
    return render(request, 'colegios/detalle.html', {'id': id})  # Asegúrate de que la plantilla exista

def crear_colegio(request):
    # Lógica para crear un nuevo colegio
    return render(request, 'colegios/crear.html')  # Asegúrate de que la plantilla exista

def editar_colegio(request, id):
    # Lógica para editar un colegio existente
    return render(request, 'colegios/editar.html', {'id': id})  # Asegúrate de que la plantilla exista