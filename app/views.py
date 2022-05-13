from django.shortcuts import render
from ninja import Router

router = Router()

@router.get('/')
def index(request):
    return render(request, 'index.html')
