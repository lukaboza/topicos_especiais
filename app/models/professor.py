from django.db import models
from app.models.federacao import Federacao


class Professor(models.Model):
    class Meta:
        db_table = 'professor'

    federacao = models.ForeignKey(Federacao, models.DO_NOTHING)
    codigo = models.CharField(max_length=45)
    nome = models.CharField(max_length=45)
    rg = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    orgao_emissor = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45)
    sexo = models.CharField(max_length=1)
    email = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    facebook = models.CharField(max_length=45, null=True)
    telefone = models.CharField(max_length=45, null=True)
    celular = models.CharField(max_length=45)
            