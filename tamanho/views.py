from rest_framework import (
    exceptions,
    status,
    viewsets,
)

from rest_framework.response import Response

from tamanho.models import Tamanho
from tamanho.serializers import TamanhoSerializer


class TamanhoViewSet(viewsets.ViewSet):
    serializer_class = TamanhoSerializer

    def list(self, request):
        tamanhos = Tamanho.objects.all()
        tamanhos_serialized = self.serializer_class(tamanhos, many=True)
        return Response(tamanhos_serialized.data, status=status.HTTP_200_OK)
