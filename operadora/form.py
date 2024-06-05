from django import forms
from .models import Operadora, Endereco


class OperadoraForm(forms.ModelForm):
    cep = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cep'}),
        required=True
    )
    rua = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua'}),
        required=True
    )
    numero = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero'}),
        required=True
    )
    complemento = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Complemento'}),
        required=False
    )
    bairro = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
        required=True
    )
    cidade = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
        required=True
    )
    uf = forms.CharField(
        widget=forms.Select(choices=[('AC', 'Acre'), ('AL', 'Alagoas')]),
        required=True
    )

    class Meta:
        model = Operadora
        fields = ['nome', 'descricao', 'razao_social', 'codigo_cnes',
                  'registro_ans', 'cnpj', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Operadora'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_cnes': forms.TextInput(attrs={'class': 'form-control'}),
            'registro_ans': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        operadora = super().save(commit=False)
        endereco_data = {
            'cep': self.cleaned_data.get('cep'),
            'rua': self.cleaned_data.get('rua'),
            'numero': self.cleaned_data.get('numero'),
            'complemento': self.cleaned_data.get('complemento'),
            'bairro': self.cleaned_data.get('bairro'),
            'cidade': self.cleaned_data.get('cidade'),
            'uf': self.cleaned_data.get('uf')
        }

        endereco, created = Endereco.objects.get_or_create(**endereco_data)
        operadora.endereco = endereco

        if commit:
            operadora.save()

        return operadora
