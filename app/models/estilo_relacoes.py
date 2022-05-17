from django.db import models
from app.models.estilo import Estilo
from app.models.professor import Professor
from app.models.escola import Escola 
from django.contrib.contenttypes.fields import GenericForeignKey


class EstiloRelacoes(models.Model):
    class Meta:
        db_table = 'estilo_relacoes'

    estilos_id = models.ForeignKey(Estilo, null=False, on_delete=models.DO_NOTHING)
    origem_tipo = models.CharField(max_length=45)
    professor_id = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    escola_id = models.ForeignKey(Escola, on_delete=models.DO_NOTHING)

    origem_id = GenericForeignKey(
        'professor_id',
        'escola_id'
    )
