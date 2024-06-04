# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PrismaMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    checksum = models.CharField(max_length=64)
    finished_at = models.DateTimeField(blank=True, null=True)
    migration_name = models.CharField(max_length=255)
    logs = models.TextField(blank=True, null=True)
    rolled_back_at = models.DateTimeField(blank=True, null=True)
    started_at = models.DateTimeField()
    applied_steps_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = '_prisma_migrations'


class Agendamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    encaixe = models.IntegerField()
    retorno = models.IntegerField()
    status = models.ForeignKey('Status', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    colaborador = models.ForeignKey('Colaborador', models.DO_NOTHING)
    especialidade = models.ForeignKey('Especialidade', models.DO_NOTHING)
    hora_fim = models.DateTimeField()
    hora_inicio = models.DateTimeField()
    local = models.ForeignKey('Local', models.DO_NOTHING)
    paciente = models.ForeignKey('Paciente', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'agendamento'


class AgendamentoServico(models.Model):
    id = models.BigAutoField(primary_key=True)
    servico = models.ForeignKey('Servico', models.DO_NOTHING)
    convenio = models.ForeignKey('Convenio', models.DO_NOTHING)
    agendamento = models.ForeignKey(Agendamento, models.DO_NOTHING)
    retorno = models.IntegerField()
    tempo = models.IntegerField()
    valor = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agendamento_servico'


class ArquivoAgendamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    caminho_arquivo = models.CharField(max_length=191)
    nome = models.CharField(max_length=191)
    extensao = models.CharField(max_length=191)
    agendamento = models.OneToOneField(Agendamento, models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arquivo_agendamento'


class ArquivoAtendimento(models.Model):
    id = models.BigAutoField(primary_key=True)
    caminho_arquivo = models.CharField(max_length=191)
    nome = models.CharField(max_length=191)
    extensao = models.CharField(max_length=191)
    atendimento = models.OneToOneField('Atendimento', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arquivo_atendimento'


class ArquivoPaciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    caminho_arquivo = models.CharField(max_length=191)
    nome = models.CharField(max_length=191)
    extensao = models.CharField(max_length=191)
    paciente = models.OneToOneField('Paciente', models.DO_NOTHING)
    colaborador_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arquivo_paciente'


class Atendimento(models.Model):
    id = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey('Paciente', models.DO_NOTHING)
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING)
    ativo = models.IntegerField()
    tipo_atendimento = models.CharField(unique=True, max_length=191)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'atendimento'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Colaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    cpf = models.CharField(unique=True, max_length=191)
    data_nascimento = models.DateTimeField()
    sexo = models.ForeignKey('Sexo', models.DO_NOTHING)
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
    endereco = models.ForeignKey('Endereco', models.DO_NOTHING)
    grupo_empresarial = models.ForeignKey('GrupoEmpresarial', models.DO_NOTHING, blank=True, null=True)
    cor_na_agenda = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colaborador'


class ColaboradorConselho(models.Model):
    id = models.BigAutoField(primary_key=True)
    registro_conselho = models.CharField(unique=True, max_length=191)
    descricao = models.CharField(max_length=191, blank=True, null=True)
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING)
    conselho = models.ForeignKey('ConselhoProfissional', models.DO_NOTHING)
    unidade_federativa = models.ForeignKey('UnidadeFederativa', models.DO_NOTHING)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'colaborador_conselho'


class ColaboradorEmpresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING)
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'colaborador_empresa'


class ColaboradorEspecialidade(models.Model):
    id = models.BigAutoField(primary_key=True)
    unidade_federativa = models.ForeignKey('UnidadeFederativa', models.DO_NOTHING)
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING)
    especialidade = models.ForeignKey('Especialidade', models.DO_NOTHING)
    rqe = models.CharField(unique=True, max_length=191)
    idade_minima_atendimento = models.IntegerField(blank=True, null=True)
    idade_maxima_atendimento = models.IntegerField(blank=True, null=True)
    anamnese_padrao = models.CharField(max_length=191, blank=True, null=True)
    evolucao_padrao = models.CharField(max_length=191, blank=True, null=True)
    observacoes = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'colaborador_especialidade'


class ColaboradorGrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    local = models.ForeignKey('Local', models.DO_NOTHING)
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING)
    inicio_atendimento = models.DateTimeField()
    fim_atendimento = models.DateTimeField()
    tempo_atendimento = models.IntegerField(blank=True, null=True)
    repetir = models.CharField(max_length=191)
    dias_da_semana = models.CharField(max_length=191)
    maximo_encaixe_por_dia = models.IntegerField()
    minimo_encaixe_por_horario = models.IntegerField()
    minimo_tempo_entre_encaixes = models.IntegerField()
    copia_id = models.CharField(max_length=191, blank=True, null=True)
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'colaborador_grade'


class ColaboradorGradeEspecialidades(models.Model):
    id = models.BigAutoField(primary_key=True)
    colaborador_grade = models.ForeignKey(ColaboradorGrade, models.DO_NOTHING)
    especialidade = models.ForeignKey(ColaboradorEspecialidade, models.DO_NOTHING)
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'colaborador_grade_especialidades'


class ConselhoProfissional(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=191)
    descricao = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'conselho_profissional'


class Contato(models.Model):
    id = models.BigAutoField(primary_key=True)
    pessoa_de_contato = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    celular = models.CharField(max_length=191)
    telefone = models.CharField(max_length=191)
    operadora = models.ForeignKey('Operadora', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contato'


class Convenio(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=191)
    codigo_ans = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    telefone = models.CharField(max_length=191, blank=True, null=True)
    field_pessoa_de_contato_field = models.CharField(db_column='(pessoa_de_contato)', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    kit_de_produtos = models.ForeignKey('KitDeProdutosId', models.DO_NOTHING, blank=True, null=True)
    tempo_retorno = models.IntegerField(blank=True, null=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(blank=True, null=True)
    data_reajuste = models.DateTimeField(blank=True, null=True)
    recurso_glosa_dias = models.IntegerField(blank=True, null=True)
    empresa_principal = models.ForeignKey('Empresa', models.DO_NOTHING)
    operadora = models.ForeignKey('Operadora', models.DO_NOTHING)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    prazo_pagamento_dias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenio'


class ConvenioColaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING)
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING)
    colaboradorexecutante = models.CharField(db_column='colaboradorExecutante', max_length=191)  # Field name made lowercase.
    colaboradorresponsavelautorizado = models.CharField(db_column='colaboradorResponsavelAutorizado', max_length=191)  # Field name made lowercase.
    created_at = models.DateTimeField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'convenio_colaborador'


class ConvenioEmpresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING)
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING)
    created_at = models.DateTimeField()
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'convenio_empresa'


class ConvenioEspecialidade(models.Model):
    id = models.BigAutoField(primary_key=True)
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING)
    especialidade = models.ForeignKey('Especialidade', models.DO_NOTHING)
    datainicio = models.DateTimeField(db_column='dataInicio', blank=True, null=True)  # Field name made lowercase.
    datafim = models.DateTimeField(db_column='dataFim', blank=True, null=True)  # Field name made lowercase.
    utiliza_especialidade = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'convenio_especialidade'


class ConvenioPlano(models.Model):
    id = models.BigAutoField(primary_key=True)
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING)
    plano = models.ForeignKey('Plano', models.DO_NOTHING)
    ultiliza_plano = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'convenio_plano'


class ConvenioProduto(models.Model):
    id = models.BigAutoField(primary_key=True)
    produto = models.ForeignKey('Produto', models.DO_NOTHING)
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING)
    utiliza_produto = models.IntegerField(blank=True, null=True)
    produto_convenio = models.CharField(db_column='Produto_Convenio', max_length=191, blank=True, null=True)  # Field name made lowercase.
    descricao_convenio = models.CharField(db_column='descricao_Convenio', max_length=191, blank=True, null=True)  # Field name made lowercase.
    codigo_tuss = models.CharField(db_column='Codigo_Tuss', max_length=191, blank=True, null=True)  # Field name made lowercase.
    codigo_tiss = models.CharField(db_column='Codigo_Tiss', max_length=191, blank=True, null=True)  # Field name made lowercase.
    datainiciovigencia = models.DateTimeField(db_column='dataInicioVigencia', blank=True, null=True)  # Field name made lowercase.
    datafimvigencia = models.DateTimeField(db_column='dataFimVigencia', blank=True, null=True)  # Field name made lowercase.
    valor_unitario_convenio = models.DecimalField(db_column='Valor_Unitario_Convenio', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'convenio_produto'


class DepositoId(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao_do_deposito = models.CharField(max_length=191)
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING, blank=True, null=True)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'deposito_id'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documento(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=191)
    ativo = models.IntegerField()
    deleted = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'documento'


class DocumentoServico(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    servico = models.ForeignKey('Servico', models.DO_NOTHING)
    documento = models.ForeignKey(Documento, models.DO_NOTHING)
    ativo = models.IntegerField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'documento_servico'


class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    razao_social = models.CharField(max_length=191)
    nome_fantasia = models.CharField(max_length=191)
    cnpj = models.CharField(max_length=191)
    ativo = models.IntegerField(blank=True, null=True)
    grupo_empresarial = models.ForeignKey('GrupoEmpresarial', models.DO_NOTHING)
    cnes = models.CharField(max_length=8)
    telefone = models.CharField(max_length=191, blank=True, null=True)
    telefone_2 = models.CharField(max_length=191, blank=True, null=True)
    celular = models.CharField(max_length=191)
    celular_2 = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191)
    email_2 = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    endereco = models.ForeignKey('Endereco', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Endereco(models.Model):
    id = models.BigAutoField(primary_key=True)
    cep = models.CharField(max_length=191)
    endereco = models.CharField(max_length=191)
    numero = models.CharField(max_length=191)
    complemento = models.CharField(max_length=191, blank=True, null=True)
    bairro = models.CharField(max_length=191)
    cidade = models.CharField(max_length=191)
    unidade_federativa = models.ForeignKey('UnidadeFederativa', models.DO_NOTHING)
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'endereco'


class Equipamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    local = models.ForeignKey('Local', models.DO_NOTHING, blank=True, null=True)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipamento'


class EquipamentoColaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipamento = models.ForeignKey(Equipamento, models.DO_NOTHING)
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipamento_colaborador'


class EquipamentoConvenio(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipamento = models.ForeignKey(Equipamento, models.DO_NOTHING)
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipamento_convenio'


class EquipamentoGrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    local = models.ForeignKey('Local', models.DO_NOTHING)
    equipamento = models.ForeignKey(Equipamento, models.DO_NOTHING)
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING, blank=True, null=True)
    profissionais = models.ForeignKey(Colaborador, models.DO_NOTHING, blank=True, null=True)
    dia_da_semana = models.CharField(max_length=191)
    inicio_atendimento = models.DateTimeField()
    fim_atendimento = models.DateTimeField()
    grade_em_minutos = models.IntegerField()
    vigente_desde = models.CharField(max_length=191, blank=True, null=True)
    vigente_ate = models.CharField(max_length=191, blank=True, null=True)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    copia_id = models.BigIntegerField(blank=True, null=True)
    repetir = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'equipamento_grade'


class EquipamentoGradeColaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipamento_grade = models.ForeignKey(EquipamentoGrade, models.DO_NOTHING)
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING)
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipamento_grade_colaborador'


class EquipamentoGradeConvenio(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipamento_grade = models.ForeignKey(EquipamentoGrade, models.DO_NOTHING)
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING)
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipamento_grade_convenio'


class EquipamentoGradeServicos(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipamento_grade = models.ForeignKey(EquipamentoGrade, models.DO_NOTHING)
    servico = models.ForeignKey('Servico', models.DO_NOTHING)
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipamento_grade_servicos'


class EquipamentoServico(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipamento = models.ForeignKey(Equipamento, models.DO_NOTHING)
    servico = models.ForeignKey('Servico', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipamento_servico'


class Especialidade(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    codigo = models.CharField(max_length=191, blank=True, null=True)
    cbos = models.CharField(max_length=191, blank=True, null=True)
    cbos_antigo = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    colaborador_grade = models.ForeignKey(ColaboradorGrade, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidade'


class Fabricante(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fabricante'


class Fornecedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    cnpj = models.CharField(max_length=191)
    inscricao = models.CharField(max_length=191)
    telefone_fornecedor = models.CharField(max_length=191)
    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, blank=True, null=True)
    ativo = models.IntegerField()
    tipo_prestador_de_servico = models.CharField(max_length=191)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fornecedor'


class FornecedorProdutos(models.Model):
    id = models.BigAutoField(primary_key=True)
    produto = models.ForeignKey('Produto', models.DO_NOTHING)
    fornecedor = models.ForeignKey(Fornecedor, models.DO_NOTHING)
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fornecedor_produtos'


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


class KitDeProdutosId(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=191)
    codigo = models.IntegerField()
    valor = models.FloatField()
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kit_de_produtos_id'


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


class Movimentacao(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantidade = models.IntegerField()
    deposito = models.ForeignKey(DepositoId, models.DO_NOTHING)
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'movimentacao'


class Operadora(models.Model):
    id = models.BigAutoField(primary_key=True)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, blank=True, null=True)
    cnpj = models.CharField(max_length=191)
    codigo_cnes = models.CharField(max_length=7)
    descricao = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    nome = models.CharField(max_length=191)
    razao_social = models.CharField(max_length=191, blank=True, null=True)
    registro_ans = models.CharField(max_length=191, blank=True, null=True)
    telefone = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operadora'


class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    rg = models.CharField(unique=True, max_length=191)
    cpf = models.CharField(unique=True, max_length=191)
    idade = models.CharField(max_length=191)
    data_nascimento = models.DateTimeField()
    sexo = models.ForeignKey('Sexo', models.DO_NOTHING)
    estrangeiro = models.IntegerField()
    estado_civil = models.CharField(max_length=191, blank=True, null=True)
    profissao = models.CharField(max_length=191, blank=True, null=True)
    atendimentorn = models.IntegerField(db_column='atendimentoRn')  # Field name made lowercase.
    email = models.CharField(max_length=191)
    email2 = models.CharField(max_length=191, blank=True, null=True)
    telefone = models.CharField(max_length=191, blank=True, null=True)
    telefone2 = models.CharField(max_length=191, blank=True, null=True)
    celular = models.CharField(max_length=191)
    celular2 = models.CharField(max_length=191, blank=True, null=True)
    endereco = models.OneToOneField(Endereco, models.DO_NOTHING)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    plano_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class PacientePlano(models.Model):
    id = models.BigAutoField(primary_key=True)
    matricula = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    validade = models.DateTimeField(blank=True, null=True)
    plano = models.ForeignKey('Plano', models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'paciente_plano'


class Plano(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    operadora = models.ForeignKey(Operadora, models.DO_NOTHING)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plano'


class PrincipioAtivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    d_e_l_e_t_e_d = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'principio_ativo'


class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    validade = models.DateTimeField()
    valor_medio = models.FloatField(blank=True, null=True)
    codigo_ean = models.CharField(max_length=191, blank=True, null=True)
    codigo_ncm = models.CharField(db_column='CODIGO_NCM', max_length=191, blank=True, null=True)  # Field name made lowercase.
    codigo_tuss = models.CharField(db_column='CODIGO_TUSS', max_length=191)  # Field name made lowercase.
    codigo_tiss = models.CharField(db_column='CODIGO_TISS', max_length=191)  # Field name made lowercase.
    codigo_produto = models.CharField(db_column='CODIGO_PRODUTO', max_length=191)  # Field name made lowercase.
    descricao = models.CharField(max_length=191, blank=True, null=True)
    numero_lote = models.CharField(db_column='NUMERO_LOTE', max_length=191)  # Field name made lowercase.
    unidade_de_medida = models.CharField(db_column='UNIDADE_DE_MEDIDA', max_length=191, blank=True, null=True)  # Field name made lowercase.
    valor_total_itens = models.FloatField(db_column='VALOR_TOTAL_ITENS', blank=True, null=True)  # Field name made lowercase.
    valor_unitario = models.FloatField(db_column='VALOR_UNITARIO')  # Field name made lowercase.
    fabricante = models.ForeignKey(Fabricante, models.DO_NOTHING)
    tipo_produto = models.ForeignKey('TipoProduto', models.DO_NOTHING)
    principio_ativo = models.ForeignKey(PrincipioAtivo, models.DO_NOTHING)
    deposito = models.ForeignKey(DepositoId, models.DO_NOTHING)
    ativo = models.IntegerField()
    d_e_l_e_t_e_d = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'produto'


class ProdutoServico(models.Model):
    id = models.BigAutoField(primary_key=True)
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    servico = models.ForeignKey('Servico', models.DO_NOTHING)
    quantidade = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=191, blank=True, null=True)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'produto_servico'


class Servico(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=191)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    codigotuss = models.CharField(db_column='codigoTUSS', max_length=11, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(max_length=191)
    valor = models.DecimalField(max_digits=65, decimal_places=30, blank=True, null=True)
    tempo_servico = models.FloatField(blank=True, null=True)
    agendamento_id = models.CharField(max_length=191, blank=True, null=True)
    tipo_servico = models.ForeignKey('TipoServico', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'servico'


class ServicoColaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    servico = models.ForeignKey(Servico, models.DO_NOTHING)
    colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'servico_colaborador'


class ServicoConvenio(models.Model):
    id = models.BigAutoField(primary_key=True)
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING)
    servico = models.ForeignKey(Servico, models.DO_NOTHING)
    data_ini_vigencia = models.DateTimeField()
    data_fim_vigencia = models.DateTimeField()
    codigo_tuss = models.CharField(max_length=191)
    utiliza_servico = models.IntegerField(blank=True, null=True)
    ativo = models.IntegerField()
    codigo_convenio = models.CharField(max_length=191)
    descricao_convenio = models.CharField(max_length=191)
    valor_interno_convenio = models.CharField(max_length=191)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'servico_convenio'


class ServicoEspecialidade(models.Model):
    id = models.BigAutoField(primary_key=True)
    servico = models.ForeignKey(Servico, models.DO_NOTHING)
    especialidade = models.ForeignKey(Especialidade, models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'servico_especialidade'


class ServicoLocal(models.Model):
    id = models.BigAutoField(primary_key=True)
    servico = models.ForeignKey(Servico, models.DO_NOTHING)
    local = models.ForeignKey(Local, models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'servico_local'


class ServicoPlano(models.Model):
    id = models.BigAutoField(primary_key=True)
    convenio_id = models.BigIntegerField()
    plano = models.ForeignKey(Plano, models.DO_NOTHING)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'servico_plano'


class Sexo(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'sexo'


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=191)
    ativo = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status'


class Taxas(models.Model):
    id = models.BigAutoField(primary_key=True)
    taxas = models.CharField(db_column='TAXAS', max_length=191)  # Field name made lowercase.
    descricao = models.CharField(max_length=191, blank=True, null=True)
    codigotaxa = models.IntegerField(db_column='CODIGOTAXA')  # Field name made lowercase.
    valor = models.DecimalField(db_column='VALOR', max_digits=65, decimal_places=30)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted = models.IntegerField()
    tipo_taxa = models.ForeignKey('TipoTaxa', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taxas'


class TipoColaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=191)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    colaborador = models.OneToOneField(Colaborador, models.DO_NOTHING)
    ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_colaborador'


class TipoProduto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    ativo = models.IntegerField(db_column='ATIVO')  # Field name made lowercase.
    d_e_l_e_t_e_d = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tipo_produto'


class TipoServico(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=191)
    ativo = models.IntegerField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_servico'


class TipoTaxa(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipotaxa = models.CharField(db_column='TIPOTAXA', max_length=191)  # Field name made lowercase.
    ativo = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_taxa'


class UnidadeFederativa(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=191)
    unidade_federativa_id = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'unidade_federativa'
