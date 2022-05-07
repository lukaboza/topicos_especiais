from django.db import models

# Create your models here.

# mock ---
class Professor(models.Model):
    nome = models.CharField(max_length=20)

class Escolas(models.Model):
    nome = models.CharField(max_length=20)


class Estilos(models.Model):
    nome = models.CharField(max_length=20)


class Alvara(models.Model):
    id_escola = models.ForeignKey(Escolas,on_delete=models.DO_NOTHING) # aqui sera o id da escola
    data_de_criacao = models.DateField()
    valido_ate = models.DateField()
    qrcode = models.ImageField()
    id_responsavel = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return "oi"


class AlvaraEstilos(models.Model):
    id_alvara = models.ForeignKey(Alvara, on_delete=models.DO_NOTHING)
    id_estilos = models.ForeignKey(Estilos, on_delete=models.DO_NOTHING)