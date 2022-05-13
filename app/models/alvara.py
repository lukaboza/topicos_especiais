from django.db import models
from app.models import responsavel_atleta

class Alvara(models.Model):
    class Meta:
        db_table = 'alvara'

    RELACAO_TIPO = (
    )

    professor = models.ForeignKey(responsavel_atleta, on_delete=models.CASCADE)

    data_de_emissao = models.DateTimeField(auto_now_add=True)
    data_de_validade = models.DateTimeField(auto_now=True)
