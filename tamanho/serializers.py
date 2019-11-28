from rest_framework import serializers
from tamanho.models import Tamanho


class TamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamanho
        fields = '__all__'