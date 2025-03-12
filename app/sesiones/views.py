from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from .models import Sesion
from .forms import SesionForm
from .serializers import SesionSerializer

# Vistas basadas en clases para la interfaz web
class SesionListView(LoginRequiredMixin, ListView):
    model = Sesion
    template_name = 'sesion_list.html'
    context_object_name = 'sesiones'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                id_alumno__alumno_nombre__icontains=search_query
            ) | queryset.filter(
                id_terapeuta__terapeuta_nombre__icontains=search_query
            ) | queryset.filter(
                id_curso__nombre_curso__icontains=search_query
            )
        return queryset

class SesionCreateView(LoginRequiredMixin, CreateView):
    model = Sesion
    form_class = SesionForm
    template_name = 'sesion_form.html'
    success_url = reverse_lazy('sesion_list')

    def form_valid(self, form):
        print("Formulario válido, datos:", form.cleaned_data)
        messages.success(self.request, "Sesión creada exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Errores en el formulario:", form.errors)
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"Error en {field}: {error}")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Añadir Sesión'
        context['boton'] = 'Crear'
        return context

class SesionUpdateView(LoginRequiredMixin, UpdateView):
    model = Sesion
    form_class = SesionForm
    template_name = 'sesion_form.html'

    def get_object(self):
        return get_object_or_404(Sesion, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('sesion_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, "Sesión actualizada exitosamente.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Sesión'
        context['boton'] = 'Guardar Cambios'
        return context

class SesionDeleteView(LoginRequiredMixin, DeleteView):
    model = Sesion
    template_name = 'sesion_confirm_delete.html'
    success_url = reverse_lazy('sesion_list')

    def get_object(self):
        return get_object_or_404(Sesion, pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Sesión eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)

class SesionDetailView(LoginRequiredMixin, DetailView):
    model = Sesion
    template_name = 'sesion_detail.html'
    context_object_name = 'sesion'

    def get_object(self):
        return get_object_or_404(Sesion, pk=self.kwargs['pk'])

# ViewSet para la API RESTful
class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer