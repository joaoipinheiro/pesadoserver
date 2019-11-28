from rest_framework import (
    exceptions,
    status,
    viewsets,
)

from rest_framework.response import Response

from sabores.models import Sabores
from sabores.serializers import SaboresSerializer


class SaboresViewSet(viewsets.ViewSet):
    serializer_class = SaboresSerializer

    def list(self, request):
        sabores = Sabores.objects.all()
        sabores_serialized = self.serializer_class(sabores, many=True)
        return Response(sabores_serialized.data, status=status.HTTP_200_OK)
