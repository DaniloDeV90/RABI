from django import forms

from .models import PrincipioAtivo


class PrincipioAtivoForm(forms.ModelForm):
    class Meta:
        model = PrincipioAtivo
        fields = ['nome']
        widgets = {

            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Principio Ativo'}),

        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if Equipamento.objects.filter(nome=nome).exists():
            raise forms.ValidationError("O nome do principio ativo deve ser único.")
        return nome