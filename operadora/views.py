from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Operadora
from operadora.form import OperadoraForm
# Post
def criar_operadora(request):
    return render(request, "operadora.html")