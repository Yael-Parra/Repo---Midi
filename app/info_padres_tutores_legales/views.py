from rest_framework import viewsets
from .models import InfoPadresTutoresLegales
from .serializers import InfoPadresTutoresLegalesSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Vistas basadas en funciones para la interfaz web
@login_required
def lista_info(request):
    info_padres_tutores = InfoPadresTutoresLegales.objects.all()
    return render(request, 'info_padres_tutores_legales/lista.html', {'info_padres_tutores': info_padres_tutores})

@login_required
def detalle_info(request, id):
    info_padres_tutores = InfoPadresTutoresLegales.objects.get(id_tutor=id)
    return render(request, 'info_padres_tutores_legales/detalle.html', {'info_padres_tutores': info_padres_tutores})

@login_required
def crear_info(request):
    if request.method == 'POST':  # ¡Aquí estaba el error! Ahora está correctamente indentado.
        id_alumno = request.POST['id_alumno']
        mama_nombre = request.POST['mama_nombre']
        mama_apellido = request.POST['mama_apellido']
        mama_cedula = request.POST['mama_cedula']
        mama_telefono = request.POST['mama_telefono']
        mama_email = request.POST['mama_email']
        mama_empresa = request.POST['mama_empresa']
        papa_nombre = request.POST['papa_nombre']
        papa_apellido = request.POST['papa_apellido']
        papa_cedula = request.POST['papa_cedula']
        papa_telefono = request.POST['papa_telefono']
        papa_email = request.POST['papa_email']
        papa_empresa = request.POST['papa_empresa']
        direccion = request.POST['direccion']
        info_padres_tutores = InfoPadresTutoresLegales.objects.create(
            id_alumno=id_alumno,
            mama_nombre=mama_nombre,
            mama_apellido=mama_apellido,
            mama_cedula=mama_cedula,
            mama_telefono=mama_telefono,
            mama_email=mama_email,
            mama_empresa=mama_empresa,
            papa_nombre=papa_nombre,
            papa_apellido=papa_apellido,
            papa_cedula=papa_cedula,
            papa_telefono=papa_telefono,
            papa_email=papa_email,
            papa_empresa=papa_empresa,
            direccion=direccion
        )
        messages.success(request, 'Información de padres/tutores creada exitosamente')
        return redirect('lista_info')
    return render(request, 'info_padres_tutores_legales/crear.html')

@login_required
def editar_info(request, id):
    info_padres_tutores = InfoPadresTutoresLegales.objects.get(id_tutor=id)
    if request.method == 'POST':
        info_padres_tutores.id_alumno = request.POST['id_alumno']
        info_padres_tutores.mama_nombre = request.POST['mama_nombre']
        info_padres_tutores.mama_apellido = request.POST['mama_apellido']
        info_padres_tutores.mama_cedula = request.POST['mama_cedula']
        info_padres_tutores.mama_telefono = request.POST['mama_telefono']
        info_padres_tutores.mama_email = request.POST['mama_email']
        info_padres_tutores.mama_empresa = request.POST['mama_empresa']
        info_padres_tutores.papa_nombre = request.POST['papa_nombre']
        info_padres_tutores.papa_apellido = request.POST['papa_apellido']
        info_padres_tutores.papa_cedula = request.POST['papa_cedula']
        info_padres_tutores.papa_telefono = request.POST['papa_telefono']
        info_padres_tutores.papa_email = request.POST['papa_email']
        info_padres_tutores.papa_empresa = request.POST['papa_empresa']
        info_padres_tutores.direccion = request.POST['direccion']
        info_padres_tutores.save()
        messages.success(request, 'Información de padres/tutores actualizada exitosamente')
        return redirect('lista_info')
    return render(request, 'info_padres_tutores_legales/editar.html', {'info_padres_tutores': info_padres_tutores})

# Vistas de la API
class InfoPadresTutoresLegalesViewSet(viewsets.ModelViewSet):
    queryset = InfoPadresTutoresLegales.objects.all()
    serializer_class = InfoPadresTutoresLegalesSerializer