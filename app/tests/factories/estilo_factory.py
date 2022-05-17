import factory
from faker import Faker
from random import sample

from app.models import Estilo

faker = Faker('pt_BR')  

class EstiloFactory(factory.Factory):
    class Meta:
        model = Estilo

    nome = faker.name()
    categoria = sample(['moderno', 'tradicional','shuaijiao','sanda','outros'], 1)[0]
    regiao = sample(['sul', 'norte','leste','sanda','oeste','outros'], 1)[0]