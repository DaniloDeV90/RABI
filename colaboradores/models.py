from django.db import models

class Colaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    cpf = models.CharField(unique=True, max_length=191)
    data_nascimento = models.DateTimeField()
    ativo = models.IntegerField()
    telefone = models.CharField(max_length=191)
    telefone2 = models.CharField(max_length=191, blank=True, null=True)
    celular = models.CharField(max_length=191)
    celular2 = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191)
    email2 = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    mensagem = models.CharField(max_length=191, blank=True, null=True)
    login = models.CharField(max_length=191)
    password = models.CharField(max_length=191)
    arquivocolaboradorpath = models.CharField(db_column='ArquivoColaboradorPath', max_length=191, blank=True, null=True)  # Field name made lowercase.
    cor_na_agenda = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colaborador'