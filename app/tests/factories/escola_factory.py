import factory
from faker import Faker

from app.models import Escola
from app.tests.factories.federacao_factory import FederacaoFactory

faker = Faker('pt_BR')

class EscolaFactory(factory.Factory):
    class Meta:
        model = Escola

    federacao = factory.SubFactory(FederacaoFactory)
    nome = faker.name()
