from rest_framework.viewsets import ModelViewSet

from core.models import Modelo
from core.serializers import ModeloDetailSerializer, ModeloListSerializer, ModeloSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return ModeloListSerializer
        elif self.action == "retrieve":
            return ModeloDetailSerializer
        return ModeloSerializer
