from django.db import models

class Federacao(models.Model):
    class Meta:
        db_table = 'federacao'

    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, db_index=True)
    email = models.CharField(max_length=255)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
