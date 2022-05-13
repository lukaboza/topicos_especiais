from django.db import models
from app.models.federacao import Federacao
from app.models.responsavel_atleta import ResponsavelAtleta

class Endereco(models.Model):
    class Meta:
        db_table = 'enderecos'

    cep = models.CharField(max_length=8, db_index=True)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=20, null=True)
    complemento = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
