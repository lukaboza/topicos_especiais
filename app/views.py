from django.shortcuts import render
from ninja import Router

router = Router()

def format_estilos(estilos):
    estilos_str = ""
    estilos_len = len(estilos)

    for idx, estilo in enumerate(estilos):
        if idx < estilos_len - 2:
            estilos_str += estilo + ", "
        elif idx == estilos_len - 2:
            estilos_str += estilo + " "
        else:
            estilos_str += "e " + estilo

    return estilos_str


@router.get('/')
def index(request):
    return render(request, 'index.html')

@router.get('/alvara')
def alvara(request):
    
    payload = {
        "nome_professor" : "Antonio",
        "rg" : "8.306.117.0",
        "orgao_emissor" : "SSP/SP",
        "estilos" : format_estilos(["Louva-a-Deus", "Shaolin-do-Norte"]),
        "validade" : "30/08/1993",
        "cidade" : "Londrina",
        "data_do_mes" : "08",
        "ano" : "2022"
    }
    return render(request, 'alvara.html', payload)