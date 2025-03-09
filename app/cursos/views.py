from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Curso
from .forms import CursoForm

# app/cursos/views.py
class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'curso_list.html'
    context_object_name = 'cursos'

    def get_queryset(self):
        queryset = super().get_queryset()
        colegio_id = self.request.GET.get('colegio')
        if colegio_id:
            queryset = queryset.filter(id_colegio=colegio_id)
        return queryset

class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form.html'
    success_url = reverse_lazy('curso_list')

    def form_valid(self, form):
        messages.success(self.request, 'Curso creado exitosamente')
        return super().form_valid(form)

class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form.html'
    success_url = reverse_lazy('curso_list')
    pk_url_kwarg = 'curso_id'

    def form_valid(self, form):
        messages.success(self.request, 'Curso actualizado exitosamente')
        return super().form_valid(form)

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'curso_confirm_delete.html'
    success_url = reverse_lazy('curso_list')
    pk_url_kwarg = 'curso_id'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Curso eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
