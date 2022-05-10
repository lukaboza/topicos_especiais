from django.db.models.signals import pre_save
from django.db import models
from django.dispatch import receiver
from app.models.federacao import Federacao
from app.models.responsavel_atleta import ResponsavelAtleta

class Atleta(models.Model):
    class Meta:
        db_table = 'atletas'

    SEXOS = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )

    federacao = models.ForeignKey(Federacao, on_delete=models.CASCADE)
    responsavel_atleta = models.ForeignKey(ResponsavelAtleta, on_delete=models.CASCADE, null=True)
    codigo = models.CharField(max_length=100, db_index=True, unique=True)
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=20, null=True, db_index=True)
    cpf = models.CharField(max_length=11, null=True, db_index=True)
    sexo = models.CharField(max_length=1, choices=SEXOS, db_index=True)
    email = models.CharField(max_length=255, null=True)
    data_nascimento = models.DateField()
    facebook = models.CharField(max_length=255, null=True)
    telefone = models.CharField(max_length=20, null=True)
    celular = models.CharField(max_length=20)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


@receiver(pre_save, sender=Atleta)
def criar_codigo(instance, **_):
    instance.codigo = Atleta.objects.count() + 1
