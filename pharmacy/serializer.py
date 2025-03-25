from rest_framework import serializers
from .models import Medicine

class Serializer(serializers.Serializer):
    class Meta:
        model = Medicine
        fields = '__all__'
