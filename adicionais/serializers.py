from rest_framework import serializers
from adicionais.models import Adicionais


class AdicionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adicionais
        fields = '__all__'