from django.db import models
from app.models.professor import Professor
from app.models.escola import Federacao

class Presidente(models.Model):
    class Meta:
        db_table = 'presidente'

    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    federacao = models.ForeignKey(Federacao, on_delete=models.DO_NOTHING)
    ativo = models.BooleanField()

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    finalizado_em = models.DateTimeField()
