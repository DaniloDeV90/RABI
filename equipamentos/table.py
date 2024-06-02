# myapp/tables.py
import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from .models import Equipamento


class EquipamentoTable(tables.Table):

    nome = tables.Column(attrs={"td": {"style": "width: 150px; overflow: hidden; text-overflow: ellipsis;"}})
    descricao = tables.Column(attrs={"td": {"style": "width: 150px; overflow: hidden; text-overflow: ellipsis;"}})
    acao = tables.TemplateColumn(
        template_code='''
          <div>
            <a href="#">Editar</a> | 
            <a href="#">Excluir</a>
        </div>
        '''
    )

    class Meta:
        model = Equipamento
        template_name = "django_tables2/bootstrap5.html"
        fields = ( "nome", "descricao", "acao")