from django.db import models
from app.models.federacao import Professor

from app.models.responsavel_atleta import ResponsavelAtleta

class Escola(models.Model):
    class Meta:
        db_table = 'escola'

    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, db_index=True)
    email = models.CharField(max_length=255)
    presidente = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
