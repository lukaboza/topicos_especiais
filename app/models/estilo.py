from django.db import models


class Estilo(models.Model):
    class Meta:
        db_table = 'estilo'

    nome = models.CharField(max_length=45)
    categoria = models.CharField(max_lenght=45)
    regiao = models.CharField(max_length=45)
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()