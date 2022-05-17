from urllib.parse import urlencode
from django.test import TestCase
from app.models.atleta import Atleta
from app.tests.factories.atleta_factory import AtletaFactory

from app.tests.factories.escola_factory import EscolaFactory
from app.tests.factories.federacao_factory import FederacaoFactory

class AtletasViewTests(TestCase):
    def test_render_form(self):
        federacao = FederacaoFactory()
        federacao.save()

        escola = EscolaFactory(nome='Escola 1', federacao=federacao)
        escola.save()

        response = self.client.get(f'/escolas/{escola.id}/atletas')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Escola 1')

    def test_submit_form_successfully(self):
        federacao = FederacaoFactory()
        federacao.save()

        escola = EscolaFactory(nome='Escola 1', federacao=federacao)
        escola.save()

        atleta = AtletaFactory(nome='Jorel')

        response = self.client.post(
            f'/escolas/{escola.id}/atletas',
            urlencode({
                "nome": atleta.nome,
                "sexo": atleta.sexo,
                "data_nascimento": atleta.data_nascimento,
                "celular": atleta.celular,
            }),
            content_type="application/x-www-form-urlencoded"
        )

        atleta_cadastrado = Atleta.objects.last()

        self.assertEqual(atleta_cadastrado.nome, atleta.nome)
        self.assertEqual(atleta_cadastrado.sexo, atleta.sexo)
        self.assertEqual(atleta_cadastrado.data_nascimento, atleta.data_nascimento)
        self.assertEqual(atleta_cadastrado.celular, atleta.celular)
        self.assertEqual(atleta_cadastrado.federacao, federacao)
