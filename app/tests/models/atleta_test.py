from django.test import TestCase

from app.tests.factories.atleta_factory import AtletaFactory
from app.tests.factories.federacao_factory import FederacaoFactory

class AtletaModelTest(TestCase):
    def test_generate_code_on_create(self):
        federacao = FederacaoFactory()
        federacao.save()
        atleta = AtletaFactory(federacao=federacao)
        atleta.save()

        self.assertEqual(atleta.codigo, 1)

    def test_generate_code_when_has_many_atleta(self):
        federacao = FederacaoFactory()
        federacao.save()

        AtletaFactory(federacao=federacao).save()

        atleta = AtletaFactory(federacao=federacao)
        atleta.save()

        self.assertEqual(atleta.codigo, 2)
