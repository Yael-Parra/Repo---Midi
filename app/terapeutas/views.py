from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Terapeuta
from .forms import TerapeutaForm

# Class-based view for listing therapists
class TerapeutaListView(ListView):
    model = Terapeuta
    template_name = 'lista_terapeutas.html'
    context_object_name = 'terapeutas'

# Class-based view to see details of a therapist
class TerapeutaDetailView(DetailView):
    model = Terapeuta
    template_name = 'detalle_terapeuta.html'
    context_object_name = 'terapeuta'
    pk_url_kwarg = 'id_terapeuta'

# Class-based view for creating a therapist
class TerapeutaCreateView(CreateView):
    model = Terapeuta
    form_class = TerapeutaForm
    template_name = 'crear_terapeuta.html'
    success_url = reverse_lazy('lista_terapeutas')

# Vista basada en clase para actualizar un terapeuta
class TerapeutaUpdateView(UpdateView):
    model = Terapeuta
    form_class = TerapeutaForm
    template_name = 'editar_terapeuta.html'
    pk_url_kwarg = 'id_terapeuta'
    success_url = reverse_lazy('lista_terapeutas')

# Vista basada en clase para eliminar un terapeuta
class TerapeutaDeleteView(DeleteView):
    model = Terapeuta
    pk_url_kwarg = 'id_terapeuta'
    success_url = reverse_lazy('lista_terapeutas')
    template_name = 'eliminar_terapeuta.html'

# También puedes añadir vistas basadas en funciones si prefieres
def buscar_terapeutas(request):
    query = request.GET.get('q', '')
    if query:
        terapeutas = Terapeuta.objects.filter(
            terapeuta_nombre__icontains=query) | Terapeuta.objects.filter(
            terapeuta_apellidos__icontains=query) | Terapeuta.objects.filter(
            terapeuta_cedula__icontains=query)
    else:
        terapeutas = Terapeuta.objects.all()
    
    return render(request, 'lista_terapeutas.html', {
        'terapeutas': terapeutas,
        'query': query
    })