from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alumno
from .forms import AlumnoForm

class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumno_list.html'
    context_object_name = 'alumnos'

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno_form.html'
    success_url = reverse_lazy('alumno_list')

class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno_form.html'
    success_url = reverse_lazy('alumno_list')
    pk_url_kwarg = 'id_alumno'

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'alumno_confirm_delete.html'
    success_url = reverse_lazy('alumno_list')
    pk_url_kwarg = 'id_alumno'

def alumno_detail(request, id_alumno):
    alumno = get_object_or_404(Alumno, id_alumno=id_alumno)
    return render(request, 'alumno_detail.html', {'alumno': alumno})