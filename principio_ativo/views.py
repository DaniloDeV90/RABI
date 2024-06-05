from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
import json
from django.shortcuts import render
from principio_ativo.form import PrincipioAtivoForm
from .models import PrincipioAtivo

# Create your views here.

def criar_principio_ativo(request):
    dataPrincipioAtivo = PrincipioAtivo.objects.all()
    colNames = ["Nome"]
    html_nav = f"""
            <div class="nav_list">
                <a href="/principio_ativo/criar/" class="nav_link active">
                 <i class='bx bx-cylinder nav_icon' ></i> <span class="nav_name">Dados cadastrais</span> 
                </a> 

            </div>
            """

    if request.method == "POST":
        form = PrincipioAtivoForm(request.POST)

        if form.is_valid():
            print("d")
            print(form)
            nome_principio_ativo = form.cleaned_data['nome']
            form.save()
            print(nome_principio_ativo)

        return render(request, 'principioAtivo.html',
                      {'form': form, "data": dataPrincipioAtivo, "colNames": colNames, "possuiSideBar": True,
                       "html_content": html_nav, "possuiVoltar": False})
    else:

        form = PrincipioAtivoForm(initial={"ativo": 1})
        return render(request, 'principioAtivo.html',
                      {'form': form, "data": dataPrincipioAtivo, "colNames": colNames, "possuiSideBar": True,
                       "html_content": html_nav, "possuiVoltar": False})
