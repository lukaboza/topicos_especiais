from django.db import models

class ResponsavelAtleta(models.Model):
    class Meta:
        db_table = 'responsavel_atletas'

    RELACAO_TIPO = (
        ('pai', 'Pai'),
        ('mae', 'Mãe'),
        ('avo', 'Avô'),
        ('avo_mae', 'Avó'),
        ('outros', 'Outros'),
    )

    nome = models.CharField(max_length=255)
    tipo_relacao = models.CharField(max_length=50, choices=RELACAO_TIPO)
    rg = models.CharField(max_length=20, db_index=True)
    cpf = models.CharField(max_length=11, db_index=True)
    email = models.CharField(max_length=255, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
