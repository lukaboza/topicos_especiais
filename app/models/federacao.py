from django.db import models
from app.models import responsavel_atleta

from app.models.responsavel_atleta import ResponsavelAtleta

class Federacao(models.Model):
    class Meta:
        db_table = 'ferecacoes'

    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, db_index=True)
    razao_social = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
