from django.db import models
from empresa.models import  Empresa
# Create your models here.

class Local(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'local'

    def __str__(self):
        return self.nome