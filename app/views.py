from django.shortcuts import render
from ninja import Router
from app.models.atleta import Atleta
from app.models.escola import Escola

router = Router()

@router.get('/escolas/{escola_id}/atletas')
def form_atleta(request, escola_id: int):
    escola = Escola.objects.get(id=escola_id)

    return render(request, 'atletas/form.html', context={'escola': escola})


@router.post('/escolas/{escola_id}/atletas')
def create_atleta(request, escola_id: int):
    federacao = Escola.objects.get(id=escola_id).federacao

    atleta = Atleta(
        nome=request.POST['nome'],
        sexo=request.POST['sexo'],
        data_nascimento=request.POST['data_nascimento'],
        celular=request.POST['celular'],
        federacao=federacao
    )
    atleta.save()

    return request.POST
