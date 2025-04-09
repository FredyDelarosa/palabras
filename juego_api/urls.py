from django.urls import path
from .views import PalabraListView, PalabraPorNivelView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('palabras/', PalabraListView.as_view(), name='palabras'),
    path('palabras/nivel/<int:nivel>/', PalabraPorNivelView.as_view(), name='palabras_por_nivel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
