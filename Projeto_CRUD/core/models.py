from django.db import models
from django.db.models.functions import Lower, Trim

class Categoria(models.Model):
    categoria = models.CharField(max_length=150)    

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower(Trim('categoria')),
                name='unique_categoria_case_insensitive',
            ),
        ]
    
    def __str__(self):
        return self.categoria

class Modelo(models.Model):
    modelo = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower(Trim('modelo')),
                'categoria',
                name='unique_modelo_categoria_case_insensitive',
            ),
        ]
        
    def __str__(self):
        return self.modelo

class Roupa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True, blank=True)
    cor = models.CharField(max_length=150)
    tamanho = models.CharField(max_length=10)
    quantidade = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['modelo', 'cor', 'tamanho'],
                name='unique_produto_estoque',
            ),
            models.CheckConstraint(
                condition=models.Q(quantidade__gte=0),
                name='quantidade_estoque_nao_negativa',
            ),
        ]
    
    def __str__(self):
        return str(self.modelo) if self.modelo else f'Roupa {self.pk}'