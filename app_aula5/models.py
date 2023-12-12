from django.db import models

class Dado(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(null=True, blank=True)
    pais = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome