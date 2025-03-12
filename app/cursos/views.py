# app/cursos/views.py
from rest_framework import viewsets
from .models import Curso
from .serializers import CursoSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CursoForm

# Vistas basadas en funciones para la interfaz web
@login_required
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})

@login_required
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso creado exitosamente')
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/crear.html', {'form': form})

@login_required
def editar_curso(request, id):
    curso = Curso.objects.get(id_curso=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso actualizado exitosamente')
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar.html', {'form': form})

@login_required
def eliminar_curso(request, id):
    curso = Curso.objects.get(id_curso=id)
    curso.delete()
    messages.success(request, 'Curso eliminado exitosamente')
    return redirect('lista_cursos')

# Vistas basadas en clases para la interfaz web
class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'cursos/curso_list.html'  # Asegúrate de que esta plantilla exista
    context_object_name = 'cursos'

class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'  # Asegúrate de que esta plantilla exista
    success_url = reverse_lazy('curso_list')

class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'  # Asegúrate de que esta plantilla exista
    success_url = reverse_lazy('curso_list')

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'  # Asegúrate de que esta plantilla exista
    success_url = reverse_lazy('curso_list')

# Vistas de la API
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer