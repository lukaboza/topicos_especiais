from django.shortcuts import render
from ninja import Router
from app.models.atleta import Atleta
# from app.models.escola import Escola
# from app.models.professor import Professor

router = Router()

@router.get('/')
def index(request):
    return render(request, 'index.html')

@router.get('/validate')
def validate(request):
    try:
        id = request.GET.get('id', None)
        tipo = request.GET.get('tipo', None)

        if not id: return render(request, 'validateQRCode/missing_param.html',{"param":"id"})
        if not tipo: return render(request, 'validateQRCode/missing_param.html',{"param":"tipo"})
        tipo = tipo.lower()

        if tipo == "atleta":
            try:
                atleta = Atleta.objects.get(id=id)
                return render(request, 'validateQRCode/index.html',{"atleta":atleta,"tipo":tipo})
            except Atleta.DoesNotExist:
                atleta = None
                return render(request, 'validateQRCode/not_found.html',{"tipo":tipo})

        # elif tipo == "escola":
        #     try:
        #         escola = Escola.objects.get(id=id)
        #         return render(request, 'validateQRCode/index.html',{"escola":escola, "tipo":tipo})
        #     except Escola.DoesNotExist:
        #         escola = None
        #         return render(request, 'validateQRCode/not_found.html',{"tipo":tipo})

        # elif tipo == "professor":
        #     try:
        #         professor = Professor.objects.get(id=id)
        #         return render(request, 'validateQRCode/index.html',{"professor":professor, "tipo":tipo})
        #     except Professor.DoesNotExist:
        #         professor = None
        #         return render(request, 'validateQRCode/not_found.html',{"tipo":tipo})

        else:
            return render(request, 'validateQRCode/not_found.html',{"tipo":tipo})
    except Exception as e:
        print(e)
        return str(e)
