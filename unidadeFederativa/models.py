from django.db import models

# Create your models here.
class UnidadeFederativa(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=191)
    unidade_federativa_id = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'unidade_federativa'

    def __str__(self):
        return self.unidade_federativa_id