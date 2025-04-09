from rest_framework import generics
from .models import Palabra
from .serializers import PalabraSerializer

class PalabraListView(generics.ListAPIView):
    serializer_class = PalabraSerializer
    queryset = Palabra.objects.all()
    filterset_fields = ['nivel']

class PalabraPorNivelView(generics.ListAPIView):
    serializer_class = PalabraSerializer

    def get_queryset(self):
        nivel = self.kwargs['nivel']
        return Palabra.objects.filter(nivel=nivel)
