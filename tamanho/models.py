from django.db import models


class Tamanho(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.IntegerField(default=0)
    tempo = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

