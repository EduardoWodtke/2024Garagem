from rest_framework.serializers import ModelSerializer

from core.models import Modelo


class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"


class ModeloDetailSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
        depth = 1


class ModeloListSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = ["id", "nome", "marca", "categoria"]
