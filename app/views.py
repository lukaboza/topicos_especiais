from django.shortcuts import render
from ninja import Router
from app.models.atleta import Atleta
from app.models.escola import Escola
from app.models.professor import Professor

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
            except Atleta.DoesNotExist:
                atleta = None
            if atleta:
                return render(request, 'validateQRCode/index.html',{"atleta":atleta})
            else:
                return render(request, 'validateQRCode/not_found.html',{"tipo":tipo})
        elif tipo == "escola":
            return render(request, 'validateQRCode/index.html')
        elif tipo == "professor":
            return render(request, 'validateQRCode/index.html')
        else:
            return render(request,'validateQRCode/not_found.html')
    except Exception as e:
        print(e)
        return str(e)
