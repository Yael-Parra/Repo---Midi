# app/terapeutas/views.py

from django.shortcuts import render, redirect
from .models import Terapeuta  # Asegúrate de que el modelo esté importado


def lista_terapeutas(request):
    terapeutas = Terapeuta.objects.all()
    return render(request, 'terapeutas/lista_terapeutas.html', {'terapeutas': terapeutas}) # Asegúrate de que la plantilla exista

def lista_terapeutas(request):
    # Lógica para listar terapeutas
    return render(request, 'terapeutas/lista.html')  # Asegúrate de que la plantilla exista

def detalle_terapeuta(request, id):
    # Lógica para obtener el detalle de un terapeuta específico
    return render(request, 'terapeutas/detalle.html', {'id': id})  # Asegúrate de que la plantilla exista

def crear_terapeuta(request):
    # Lógica para crear un nuevo terapeuta
    return render(request, 'terapeutas/crear.html')  # Asegúrate de que la plantilla exista

def editar_terapeuta(request, id):
    # Lógica para editar un terapeuta existente
    return render(request, 'terapeutas/editar.html', {'id': id})  # Asegúrate de que la plantilla exista

def eliminar_terapeuta(request, id):
    # Lógica para eliminar un terapeuta
    terapeuta = Terapeuta.objects.get(id=id)  # Obtén el terapeuta por ID
    terapeuta.delete()  # Elimina el terapeuta
    return redirect('lista_terapeutas')  # Redirige a la lista de terapeutas