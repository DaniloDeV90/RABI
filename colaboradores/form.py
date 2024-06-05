from django import forms
from .models import Colaborador


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control colabForm', 'placeholder': 'Nome do Colaborador'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control colabForm', 'placeholder': 'CPF do colaborador'}),

        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if Colaborador.objects.filter(nome=nome).exists():
            raise forms.ValidationError("O nome do colaborador deve ser único.")
        return nome
