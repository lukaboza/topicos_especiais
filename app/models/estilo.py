from django.db import models

class Estilo(models.Model):
    class Meta:
        db_table = 'estilos'

    CATEGORIA_TIPO = (
        ('moderno', 'Moderno'),
        ('tradicional', 'Tradicional'),
        ('shuaijiao', 'ShuaiJiao'),
        ('sanda', 'Sanda'),
        ('outros', 'Outros'),
    )
    REGIAO_ORIGEM = (
        ('sul', 'Sul'),
        ('norte', 'Norte'),
        ('leste', 'Leste'),
        ('oeste', 'Oeste'),
        ('outros', 'Outros'),
    )

    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_TIPO)
    regiao = models.CharField(max_length=50, choices=REGIAO_ORIGEM)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)