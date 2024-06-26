import uuid


from django.db import models
from local.models import Local
class Equipamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    local = models.ForeignKey(Local, models.DO_NOTHING, blank=True, null=True)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipamento'
