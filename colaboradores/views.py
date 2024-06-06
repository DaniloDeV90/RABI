from django.shortcuts import render
from .models import Colaborador
from colaboradores.form import ColaboradorForm
def criar_colaborador(request):

    html_nav = f"""
        <div class="nav_list">
            <a href="/colaboradores/criar/" class="nav_link active">
             <i class='bx bx-cylinder nav_icon' ></i> <span class="nav_name">Dados cadastrais</span> 
            </a> 
            <a href="#" class="nav_link"> 
               <i class='bx bx-time  nav_icon'></i> <span class="nav_name">Grade Horária</span> 
            </a> 

        </div>
        """

    if request.method == "POST":
        form = ColaboradorForm(request.POST)

        if form.is_valid():
            nome_equipamento = form.cleaned_data['nome']
            form.save()
            print(nome_equipamento)

        return render(request, 'colaboradores.html',{'form': form, "possuiSideBar": True, "html_content":html_nav, "possuiVoltar": False })
    else:
        form = ColaboradorForm()
        return render(request, 'colaboradores.html',{'form': form,  "possuiSideBar": True, "html_content":html_nav, "possuiVoltar": False})
