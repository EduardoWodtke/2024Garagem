from django.db import models

from .categoria import Categoria
from .marca import Marca


class Modelo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="Modelo", blank=True, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="Modelo", blank=True, null=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome.upper()}. Marca:{self.marca} e categoria:{self.categoria} ({self.id})"
