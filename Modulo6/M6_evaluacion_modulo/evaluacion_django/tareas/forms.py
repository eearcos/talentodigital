from django import forms

class TareaForm(forms.Form):
    titulo = forms.CharField(label="Título", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))