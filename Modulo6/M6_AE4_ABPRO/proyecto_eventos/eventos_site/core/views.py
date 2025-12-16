from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Evento
from .forms import EventoForm

class ListaEventos(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'core/lista_eventos.html'
    context_object_name = 'eventos'
    login_url = '/accounts/login/'

class CrearEvento(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'core/registro.html'
    success_url = reverse_lazy('lista_eventos')
    permission_required = 'core.add_evento' # Permiso necesario
    
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para crear eventos.")
        return super().handle_no_permission()

# 3. EDITAR (Acceso: Solo Organizadores y Admin)
class EditarEvento(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'core/registro.html'
    success_url = reverse_lazy('lista_eventos')
    permission_required = 'core.change_evento'

    def handle_no_permission(self):
        messages.error(self.request, "No puedes editar este evento.")
        return super().handle_no_permission()

class EliminarEvento(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Evento
    template_name = 'core/eliminar_confirmar.html'
    success_url = reverse_lazy('lista_eventos')
    permission_required = 'core.delete_evento'

    def handle_no_permission(self):
        messages.error(self.request, "Solo los administradores pueden eliminar eventos.")
        return super().handle_no_permission()