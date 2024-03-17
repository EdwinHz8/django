from django.shortcuts import render, HttpResponse, get_list_or_404
from col.models import *
from django.contrib  import messages

# Create your views here.

def getAprendices(request):
    aprendices=Aprendiz.objects.all()
    return render(request, 'index.html', {'aprendices': aprendices})


def hello_world (request):
    return HttpResponse("Pruebas")