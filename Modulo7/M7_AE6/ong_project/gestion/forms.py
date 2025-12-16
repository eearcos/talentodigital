from django import forms
from .models import Voluntario, Evento

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = '__all__'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'voluntarios': forms.CheckboxSelectMultiple()
        }