from django.test import TestCase

from app.tests.factories.atleta_factory import AtletaFactory

class AtletaModelTest(TestCase):
    def test_generate_code_on_create(self):
        atleta = AtletaFactory()
        atleta.save()

        self.assertEqual(atleta.codigo, 1)

    def test_generate_code_when_has_many_atleta(self):
        AtletaFactory().save()

        atleta = AtletaFactory()
        atleta.save()

        self.assertEqual(atleta.codigo, 2)
