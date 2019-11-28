from rest_framework import (
    exceptions,
    status,
    viewsets,
)

from rest_framework.response import Response

from adicionais.models import Adicionais
from adicionais.serializers import AdicionaisSerializer


class AdicionaisViewSet(viewsets.ViewSet):
    serializer_class = AdicionaisSerializer

    def list(self, request):
        adicionais = Adicionais.objects.all()
        adicionais_serialized = self.serializer_class(adicionais, many=True)
        return Response(adicionais_serialized.data, status=status.HTTP_200_OK)
