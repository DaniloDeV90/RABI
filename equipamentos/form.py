from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if Equipamento.objects.filter(nome=nome).exists():
            raise forms.ValidationError("O nome do equipamento deve ser único.")
        return nome
