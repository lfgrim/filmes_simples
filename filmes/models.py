from django.db import models

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=80)
    ano = models.IntegerField()
    assistido = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo