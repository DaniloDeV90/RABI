import uuid


from django.db import models
from local.models import Local
class Equipamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191, null=False, blank=False)
    local = models.ForeignKey(Local, models.DO_NOTHING, blank=True, null=True)
    ativo = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'equipamento'

    def __str__(self):
        return f"{self.nome} - {self.local}"

