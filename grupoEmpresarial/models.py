from django.db import models
from endereco.models import Endereco
# Create your models here.
class GrupoEmpresarial(models.Model):
    id = models.BigAutoField(primary_key=True)
    razao_social = models.CharField(max_length=191)
    nome_fantasia = models.CharField(max_length=191)
    cnpj = models.CharField(max_length=191, blank=True, null=True)
    cnes = models.CharField(max_length=8)
    telefone = models.CharField(max_length=191, blank=True, null=True)
    celular = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    observacoes = models.CharField(max_length=191)
    sigla = models.CharField(max_length=191)
    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, blank=True, null=True)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'grupo_empresarial'


    def __str__(self):
        return self.nome_fantasia