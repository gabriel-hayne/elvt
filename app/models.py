from django.db import models


class Person(models.Model):
    numero_inscricao = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    cep = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
