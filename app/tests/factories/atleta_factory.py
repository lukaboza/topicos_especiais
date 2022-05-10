from random import sample
import re
import factory
from faker import Faker

from app.models import Atleta

faker = Faker('pt_BR')

class AtletaFactory(factory.Factory):
    class Meta:
        model = Atleta

    nome = faker.name()
    rg = None
    cpf = re.sub('\D', '', faker.cpf())
    sexo = sample(['m', 'f'], 1)[0]
    email = faker.email()
    data_nascimento = faker.date_of_birth()
    facebook = None
    telefone = None
    celular = faker.cellphone_number()
