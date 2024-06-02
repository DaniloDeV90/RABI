import uuid

from django.db import models

# Create your models here.
from django.db import models

class Equipamento (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255, db_column='nome', unique=True)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        # Define o nome da tabela como "equipamento" no banco de dados
        db_table = 'equipamento'