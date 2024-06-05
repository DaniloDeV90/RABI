from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from .models import Equipamento
from django.shortcuts import redirect
import json
from django.shortcuts import render
from equipamentos.form import EquipamentoForm
from django.shortcuts import render, redirect, get_object_or_404

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
def criar_equipamento(request):

    colNames = ["Nome", "Local", "Ação"]

    dataEquipamento = Equipamento.objects.all()
    if request.method == "POST":
        form = EquipamentoForm(request.POST)

        if form.is_valid():
            equipamento = form.save()
            print (equipamento.id)
            return redirect(f'/equipamentos/{equipamento.id}/editar')

        return  render(request, 'equipamentos.html',{'form': form,"method":"POST", "data":dataEquipamento,"colNames": colNames, "possuiSideBar": True, "html_content":html_nav, "possuiVoltar": False })
    else:

        form = EquipamentoForm(initial={"ativo": 1})
        return  render(request, 'equipamentos.html',{'form': form,"data":dataEquipamento,"method":"POST","colNames": colNames,  "possuiSideBar": True, "html_content":html_nav, "possuiVoltar": False})


def editar_equipamento(request, id):
    dataEquipamento = Equipamento.objects.all()
    colNames = ["Nome", "Local", "Ação"]
    equipamento = get_object_or_404(Equipamento, pk=id)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamentos.html', {'form': form,"data":dataEquipamento,"method":"POST","colNames": colNames,  "possuiSideBar": True, "html_content":html_nav, "possuiVoltar": False, "nomeEpto":equipamento.nome })


def deletar_equipamento(request, id):

    equipamento = get_object_or_404(Equipamento, pk=id)
    equipamento.delete()

    return redirect(f'/equipamentos/criar')


