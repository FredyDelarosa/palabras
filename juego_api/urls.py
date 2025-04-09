from django.urls import path 
from .views import PalabraListView, PalabraPorNivelView

urlpatterns = [ 
    path('palabras/', PalabraListView.as_view(), name='palabras'), 
    path('palabras/nivel/int:nivel/', PalabraPorNivelView.as_view(), name='palabras_por_nivel'), 
    ]