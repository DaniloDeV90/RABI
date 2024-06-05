from django.db import models

from unidadeFederativa.models import UnidadeFederativa
# Create your models here.
class Endereco(models.Model):
    id = models.BigAutoField(primary_key=True)
    cep = models.CharField(max_length=191)
    endereco = models.CharField(max_length=191)
    numero = models.CharField(max_length=191)
    complemento = models.CharField(max_length=191, blank=True, null=True)
    bairro = models.CharField(max_length=191)
    cidade = models.CharField(max_length=191)
    unidade_federativa = models.ForeignKey(UnidadeFederativa, models.DO_NOTHING)
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'endereco'

    def __str__(self):
        return f"{self.cep} - {self.endereco} ({self.numero})"