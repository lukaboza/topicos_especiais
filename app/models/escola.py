from django.db import models
from app.models.federacao import Federacao


class Escola(models.Model):
    class Meta:
        db_table = 'escola'

    federacao = models.ForeignKey(Federacao, models.DO_NOTHING)
    razao_social = models.CharField(max_length=45)
    nome_fantasia = models.CharField(max_lenght=45)