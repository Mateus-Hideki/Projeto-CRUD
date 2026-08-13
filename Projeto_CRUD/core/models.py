from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=150)    
    
    def __str__(self):
        return self.categoria

class Modelo(models.Model):
    modelo = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
        
    def __str__(self):
        return self.modelo

class Roupa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    cor = models.CharField(max_length=150)
    tamanho = models.CharField(max_length=10)
    quantidade = models.IntegerField(default=1)
    
    def __str__(self):
        return self.modelo