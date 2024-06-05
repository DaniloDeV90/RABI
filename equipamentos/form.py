from django import forms

from .models import Equipamento


class EquipamentoForm(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = ['nome', 'local']

        widgets = {

            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Equipamento'}),
            'local': forms.Select(attrs={'class': 'form-control', 'value': 'Nome do Equipamento'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if Equipamento.objects.filter(nome=nome).exists():
            raise forms.ValidationError("O nome do equipamento deve ser único.")
        return nome