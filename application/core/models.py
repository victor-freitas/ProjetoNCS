# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cpf_cnpj = models.IntegerField(db_column='CPF_CNPJ', unique=True)  # Field name made lowercase.
    #nome = models.CharField(db_column='NOME', max_length=100)  # Field name made lowercase.
    razao = models.CharField(db_column='RAZAO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=80)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=200)  # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=11)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', max_length=11, blank=True, null=True)  # Field name made lowercase.
    id_seguimento = models.ForeignKey('Tiposeguimento', models.DO_NOTHING, db_column='ID_SEGUIMENTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'

    def __str__(self):
        return self.razao


class Fornecedor(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cpf_cnpj = models.IntegerField(db_column='CPF_CNPJ', unique=True)  # Field name made lowercase.
    #nome = models.CharField(db_column='NOME', max_length=100)  # Field name made lowercase.
    razao = models.CharField(db_column='RAZAO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=80)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=200)  # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=11)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', max_length=11, blank=True, null=True)  # Field name made lowercase.
    pessoa_contato = models.CharField(db_column='PESSOA_CONTATO', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fornecedor'

    def __str__(self):
        return self.razao

class Funcionario(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100)  # Field name made lowercase.
    cpf = models.IntegerField(db_column='CPF')  # Field name made lowercase.
    cargo = models.SmallIntegerField(db_column='CARGO')  # Field name made lowercase.
    id_setor = models.ForeignKey('Setor', models.DO_NOTHING, db_column='ID_SETOR')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=100)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Funcionario'


class Materiaprima(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60)  # Field name made lowercase.
    forma_emb = models.CharField(db_column='FORMA_EMB', max_length=60)  # Field name made lowercase.
    peso = models.CharField(db_column='PESO', max_length=20)  # Field name made lowercase.
    unid_medida = models.CharField(db_column='UNID_MEDIDA', max_length=50)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='QUANTIDADE')  # Field name made lowercase.
    quantidade_min = models.IntegerField(db_column='QUANTIDADE_MIN')  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=500)  # Field name made lowercase.
    data_recebimento = models.DateField(db_column='DATA_RECEBIMENTO')  # Field name made lowercase.
    id_fornecedor = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='ID_FORNECEDOR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MateriaPrima'

    def __str__(self):
        return self.nome

class Ordemdeproducao(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=500)  # Field name made lowercase.
    id_status = models.ForeignKey('Statusordemproducao', models.DO_NOTHING, db_column='ID_STATUS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrdemDeProducao'


class Pedido(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data_pedido = models.DateField(db_column='DATA_PEDIDO')  # Field name made lowercase.
    valor = models.CharField(db_column='VALOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ID_CLIENTE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pedido'


class Pedidomp(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data_pedido = models.DateField(db_column='DATA_PEDIDO')  # Field name made lowercase.
    data_prevista = models.DateField(db_column='DATA_PREVISTA')  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    valor = models.CharField(db_column='VALOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_fornecedor = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='ID_FORNECEDOR')  # Field name made lowercase.
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='ID_FUNCIONARIO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PedidoMP'


class Produto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60)  # Field name made lowercase.
    forma_emb = models.CharField(db_column='FORMA_EMB', max_length=60)  # Field name made lowercase.
    peso = models.CharField(db_column='PESO', max_length=20)  # Field name made lowercase.
    unid_medida = models.CharField(db_column='UNID_MEDIDA', max_length=50)  # Field name made lowercase.
    id_tipo = models.ForeignKey('Tipoproduto', models.DO_NOTHING, db_column='ID_TIPO')  # Field name made lowercase.
    preco = models.CharField(db_column='PRECO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='QUANTIDADE', blank=True, null=True)  # Field name made lowercase.
    desc_produto = models.CharField(db_column='DESC_PRODUTO', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Produto'


class Setor(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Setor'


class Statusordemproducao(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status_nome = models.CharField(db_column='STATUS_NOME', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StatusOrdemProducao'


class Tipoproduto(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoProduto'


class Tiposeguimento(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoSeguimento'
