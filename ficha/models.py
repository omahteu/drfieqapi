from django.db import models


class Article(models.Model):
    objects = None
    nome = models.CharField(max_length=50, blank=True)
    sobrenome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=11, blank=True)
    nascimento = models.CharField(max_length=10, blank=True)
    membro = models.CharField(max_length=7, blank=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome
