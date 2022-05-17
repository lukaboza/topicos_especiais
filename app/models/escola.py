from django.db import models
from app.models.federacao import Federacao

class Escola(models.Model):
    class Meta:
        db_table = 'escolas'

    federacao = models.ForeignKey(Federacao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
