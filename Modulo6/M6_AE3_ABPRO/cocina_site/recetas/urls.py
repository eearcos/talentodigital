from django.urls import path
from .views import InicioView, RecetaDetalleView, ContactoView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('receta/<int:pk>/', RecetaDetalleView.as_view(), name='detalle_receta'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
]