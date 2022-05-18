from django.db import models
from app.models.professor import Professor
from app.models.escola import Escola


class EscolaProfessor(models.Model):
    class Meta:
        db_table = 'escola_professor'

    escola = models.ForeignKey(Escola, models.DO_NOTHING)
    professor = models.ForeignKey(Professor, models.DO_NOTHING)
    responsavel = models.BooleanField()