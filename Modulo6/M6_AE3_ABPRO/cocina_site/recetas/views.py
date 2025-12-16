from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Receta
from .forms import ContactoForm

class InicioView(ListView):
    model = Receta
    template_name = 'home.html'
    context_object_name = 'lista_recetas'

class RecetaDetalleView(DetailView):
    model = Receta
    template_name = 'detalle.html'
    context_object_name = 'receta'

class ContactoView(FormView):
    template_name = 'contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        messages.success(self.request, "¡Mensaje enviado con éxito!")
        return super().form_valid(form)