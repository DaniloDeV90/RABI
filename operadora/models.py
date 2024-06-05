from django.db import models

from endereco.models import Endereco


class Operadora(models.Model):
    id = models.BigAutoField(primary_key=True)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, blank=True, null=True)
    cnpj = models.CharField(max_length=191)
    codigo_cnes = models.CharField(max_length=7)
    descricao = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    nome = models.CharField(max_length=191)
    razao_social = models.CharField(max_length=191, blank=True, null=True)
    registro_ans = models.CharField(max_length=191, blank=True, null=True)
    telefone = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operadora'
