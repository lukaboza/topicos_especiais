from django.db import models

# Create your models here.


class Endereco(models.Model):
    rua = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    complemento = models.CharField(max_length=20)

    cep = models.CharField(max_length=8)

    def __str__(self):
        return "oi"

class Alvara(models.Model):
    id_escola = models.CharField(max_length=30) # aqui sera o id da escola
    data_de_criacao = models.DateField()
    qrcode = models.ImageField()
    estilo = models.CharField(max_length=30)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return "oi"