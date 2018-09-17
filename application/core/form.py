from django import forms
from application.core.models import Fornecedor, Cliente, Materiaprima, Produto


class FormFornecedor(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields =    ['id','cpf_cnpj', 'razao','endereco','cep','email','telefone','celular','pessoa_contato']

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['id','cpf_cnpj','razao','endereco','cep','email','telefone','celular','id_seguimento']

class FormMateriaPrima(forms.ModelForm):
    class Meta:
        model = Materiaprima
        fields = ['id','nome','forma_emb','peso','unid_medida','quantidade','quantidade_min','descricao','data_recebimento','id_fornecedor']

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['id','nome','forma_emb','peso','unid_medida','quantidade','preco','desc_produto','id_tipo']
