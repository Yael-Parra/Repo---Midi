# app/info_padres_tutores_legales/views.py

from django.shortcuts import render

def lista_info(request):
    # Lógica para listar información de padres/tutores
    return render(request, 'info_padres_tutores_legales/lista.html')  # Asegúrate de que la plantilla exista

def detalle_info(request, id):
    # Lógica para obtener el detalle de la información de un padre/tutor específico
    return render(request, 'info_padres_tutores_legales/detalle.html', {'id': id})  # Asegúrate de que la plantilla exista

def crear_info(request):
    # Lógica para crear nueva información de un padre/tutor
    return render(request, 'info_padres_tutores_legales/crear.html')  # Asegúrate de que la plantilla exista

def editar_info(request, id):
    # Lógica para editar información de un padre/tutor existente
    return render(request, 'info_padres_tutores_legales/editar.html', {'id': id})  # Asegúrate de que la plantilla exista