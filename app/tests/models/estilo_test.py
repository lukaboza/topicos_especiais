from django.test import TestCase

from app.tests.factories.estilo_factory import EstiloFactory

class EstiloModelTest(TestCase):
    def test_generate_code_on_create(self):
        estilo = EstiloFactory()
        estilo.save()

        self.assertEqual(estilo.codigo, 1)

    def test_generate_code_when_has_many_estilo(self):
        estilo = EstiloFactory()
        estilo.save()

        self.assertEqual(estilo.codigo, 2)