from django.db import models

class Roupa(models.Model):
    categoria = models.CharField(max_length=150)
    modelo = models.CharField(max_length=150)
    cor = models.CharField(max_length=150)
    tamanho = models.CharField(max_length=10)
    quantidade = models.IntegerField(default=1)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.modelo