from rest_framework import serializers
from .models import Palabra

class PalabraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palabra
        fields = '__all__'
