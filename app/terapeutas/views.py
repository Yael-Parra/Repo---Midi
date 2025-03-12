from django.shortcuts import render, redirect
from .models import Terapeuta
from rest_framework import viewsets
from .serializers import TerapeutaSerializer

# Vistas basadas en funciones para la interfaz web
def lista_terapeutas(request):
    terapeutas = Terapeuta.objects.all()
    return render(request, 'lista_terapeutas.html', {'terapeutas': terapeutas})

def detalle_terapeuta(request, id):
    terapeuta = Terapeuta.objects.get(id_terapeuta=id)
    return render(request, 'detalle_terapeuta.html', {'terapeuta': terapeuta})

def crear_terapeuta(request):
    if request.method == 'POST':
        nombre = request.POST['terapeuta_nombre']
        apellidos = request.POST['terapeuta_apellidos']
        cedula = request.POST['terapeuta_cedula']
        telefono = request.POST['terapeuta_telefono']
        email = request.POST['terapeuta_email']
        terapeuta = Terapeuta.objects.create(
            terapeuta_nombre=nombre,
            terapeuta_apellidos=apellidos,
            terapeuta_cedula=cedula,
            terapeuta_telefono=telefono,
            terapeuta_email=email
        )
        return redirect('lista_terapeutas')
    return render(request, 'crear_terapeuta.html')

def editar_terapeuta(request, id):
    terapeuta = Terapeuta.objects.get(id_terapeuta=id)
    if request.method == 'POST':
        terapeuta.terapeuta_nombre = request.POST['terapeuta_nombre']
        terapeuta.terapeuta_apellidos = request.POST['terapeuta_apellidos']
        terapeuta.terapeuta_cedula = request.POST['terapeuta_cedula']
        terapeuta.terapeuta_telefono = request.POST['terapeuta_telefono']
        terapeuta.terapeuta_email = request.POST['terapeuta_email']
        terapeuta.save()
        return redirect('lista_terapeutas')
    return render(request, 'editar_terapeuta.html', {'terapeuta': terapeuta})

def eliminar_terapeuta(request, id):
    terapeuta = Terapeuta.objects.get(id_terapeuta=id)
    terapeuta.delete()
    return redirect('lista_terapeutas')

# Vista basada en clases para la API RESTful
class TerapeutaViewSet(viewsets.ModelViewSet):
    queryset = Terapeuta.objects.all()
    serializer_class = TerapeutaSerializer