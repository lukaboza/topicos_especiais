from urllib.parse import urlencode
from django.test import TestCase
from app.models.estilo import Estilo
from app.tests.factories.estilo_factory import EstiloFactory

class EstilosViewTests(TestCase):
    def test_render_form(self):
        response = self.client.get('/estilos')
        self.assertEqual(response.status_code, 200)

    def test_submit_form_successfully(self):

        Estilo = EstiloFactory(nome='Jorel')

        response = self.client.post(
            '/estilos',
            urlencode({
                "nome": estilo.nome,
                "categoria": estilo.categoria,
                "regiao": estilo.regiao,
            }),
            content_type="application/x-www-form-urlencoded"
        )

        estilo_cadastrado = Estilo.objects.last()

        self.assertEqual(estilo_cadastrado.nome, estilo.nome)
        self.assertEqual(estilo_cadastrado.regiao, estilo.regiao)
        self.assertEqual(estilo_cadastrado.categoria, estilo.categoria)
