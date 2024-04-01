from django.db import models

from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="Veiculo", blank=True, null=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="Veiculo", blank=True, null=True)

    def __str__(self):
        return f"({self.id}) {self.nome.upper()}, {self.modelo}, {self.cor}"
