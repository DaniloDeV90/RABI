from django.db import models
from grupoEmpresarial.models import GrupoEmpresarial
from endereco.models import Endereco
# Create your models here.
class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    razao_social = models.CharField(max_length=191)
    nome_fantasia = models.CharField(max_length=191)
    cnpj = models.CharField(max_length=191)
    ativo = models.IntegerField(blank=True, null=True)
    grupo_empresarial = models.ForeignKey(GrupoEmpresarial, models.DO_NOTHING)
    cnes = models.CharField(max_length=8)
    telefone = models.CharField(max_length=191, blank=True, null=True)
    telefone_2 = models.CharField(max_length=191, blank=True, null=True)
    celular = models.CharField(max_length=191)
    celular_2 = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191)
    email_2 = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'