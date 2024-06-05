from django.db import models


class PrincipioAtivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    d_e_l_e_t_e_d = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'principio_ativo'