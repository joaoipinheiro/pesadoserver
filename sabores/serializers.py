from rest_framework import serializers
from sabores.models import Sabores


class SaboresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sabores
        fields = '__all__'