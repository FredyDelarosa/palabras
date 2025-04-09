from rest_framework import serializers
from .models import Palabra

class PalabraSerializer(serializers.ModelSerializer):
    imagen_url = serializers.ImageField(use_url=True)
        
    class Meta:
        model = Palabra
        fields = '__all__'
