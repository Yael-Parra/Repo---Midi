# app/colegios/views.py




from rest_framework import viewsets
from .models import Colegio
from .serializers import ColegioSerializer
from django.shortcuts import render

# Vistas basadas en funciones para la interfaz web
def lista_colegios(request):
    colegios = Colegio.objects.all()
    return render(request, 'colegios/lista.html', {'colegios': colegios})

def detalle_colegio(request, id):
    colegio = Colegio.objects.get(id_colegio=id)
    return render(request, 'colegios/detalle.html', {'colegio': colegio})

def crear_colegio(request):
    if request.method == 'POST':
        nombre_colegio = request.POST['nombre_colegio']
        colegio = Colegio.objects.create(nombre_colegio=nombre_colegio)
        return redirect('lista_colegios')
    return render(request, 'colegios/crear.html')

def editar_colegio(request, id):
    colegio = Colegio.objects.get(id_colegio=id)
    if request.method == 'POST':
        colegio.nombre_colegio = request.POST['nombre_colegio']
        colegio.save()
        return redirect('lista_colegios')
    return render(request, 'colegios/editar.html', {'colegio': colegio})

# Vistas de la API
class ColegioViewSet(viewsets.ModelViewSet):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer

# from django.shortcuts import render

# def lista_colegios(request):
#     # Lógica para listar colegios
#     return render(request, 'colegios/lista.html')  # Asegúrate de que la plantilla exista

# def detalle_colegio(request, id):
#     # Lógica para obtener el detalle de un colegio específico
#     return render(request, 'colegios/detalle.html', {'id': id})  # Asegúrate de que la plantilla exista

# def crear_colegio(request):
#     # Lógica para crear un nuevo colegio
#     return render(request, 'colegios/crear.html')  # Asegúrate de que la plantilla exista

# def editar_colegio(request, id):
#     # Lógica para editar un colegio existente
#     return render(request, 'colegios/editar.html', {'id': id})  # Asegúrate de que la plantilla exista