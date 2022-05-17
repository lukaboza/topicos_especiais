import factory
from faker import Faker

from app.models import Federacao

faker = Faker('pt_BR')

class FederacaoFactory(factory.Factory):
    class Meta:
        model = Federacao

    nome_fantasia = faker.name()
    razao_social = faker.name()
    cnpj = faker.company_id()
    email = faker.company_email()
