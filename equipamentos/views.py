from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from .table import EquipamentoTable
import json
from django.shortcuts import render
from equipamentos.form import EquipamentoForm
from .models import Equipamento

# Create your views here.



def tabelaEquipamento(request):
    queryset = Equipamento.objects.all()  # Obtenha o queryset de Equipamento
    table = EquipamentoTable(queryset)  # Crie uma instância da tabela com o queryset
    table.paginate(page=request.GET.get('page', 1), per_page=25)  # Paginar a tabela

    return render(request, 'telateste.html', {'table': table})



def criar_equipamento(request):
    queryset = Equipamento.objects.all()
    table = EquipamentoTable(queryset)
    table.paginate(page=request.GET.get('page', 1), per_page=20)



    print (request.path)

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
            nome_equipamento = form.cleaned_data['nome']
            form.save()
            print(nome_equipamento)

        return  render(request, 'equipamentos.html',{'form': form,'table': table, "possuiSideBar": True, "html_content":html_nav, "possuiVoltar": False })
    else:
        form = EquipamentoForm()
        return  render(request, 'equipamentos.html',{'form': form,'table': table,  "possuiSideBar": True, "html_content":html_nav, "possuiVoltar": False})