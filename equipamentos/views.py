from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from .models import Equipamento

import json
from django.shortcuts import render
from equipamentos.form import EquipamentoForm

def criar_equipamento(request):
    dataEquipamento = Equipamento.objects.all()
    colNames = ["Nome", "Local", "Ação"]
    html_nav = f"""
        <div class="nav_list">
            <a href="/equipamentos/criar/" class="nav_link active">
             <i class='bx bx-cylinder nav_icon' ></i> <span class="nav_name">Dados cadastrais</span> 
            </a> 
            <a href="#" class="nav_link"> 
               <i class='bx bx-time  nav_icon'></i> <span class="nav_name">Grade Horária</span> 
            </a> 

        </div>
        """

    if request.method == "POST":
        form = EquipamentoForm(request.POST)

        if form.is_valid():
            print("d")
            print (form)
            nome_equipamento = form.cleaned_data['nome']
            form.save()
            print(nome_equipamento)

        return  render(request, 'equipamentos.html',{'form': form, "data":dataEquipamento,"colNames": colNames, "possuiSideBar": True, "html_content":html_nav, "possuiVoltar": False })
    else:

        form = EquipamentoForm(initial={"ativo": 1})
        return  render(request, 'equipamentos.html',{'form': form,"data":dataEquipamento,"colNames": colNames,  "possuiSideBar": True, "html_content":html_nav, "possuiVoltar": False})