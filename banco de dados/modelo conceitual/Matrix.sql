create database projeto;

USE projeto;
#1
CREATE TABLE IF NOT EXISTS Cliente(
	cpf VARCHAR(14) NOT NULL,
	primeironome VARCHAR(100) NOT NULL,
	segundonome VARCHAR(100),
	idadecliente INT NOT NULL,
	descricaocliente VARCHAR(500),
	CONSTRAINT PK_Cliente PRIMARY KEY (cpf)
);
#2
CREATE TABLE IF NOT EXISTS Fornecedor(
	cnpj VARCHAR(14) NOT NULL,
	nomeforn VARCHAR(100) NOT NULL,
	descricaofornecedor VARCHAR(500),
	CONSTRAINT PK_Fornecedor PRIMARY KEY (cnpj)
);
#3
CREATE TABLE IF NOT EXISTS Pedido(
	idpedido SMALLINT NOT NULL,
	descricaopedido VARCHAR(500) NOT NULL,
	datapedido DATE NOT NULL,
	prazopedido DATE,
	cpf VARCHAR(14) NOT NULL,
	CONSTRAINT PK_Pedido PRIMARY KEY (idpedido),
	FOREIGN KEY FK_Pedido(cpf) REFERENCES Cliente(cpf)
);
#6
CREATE TABLE IF NOT EXISTS EstoqueMateriaPrima(
	numeroestoquemateriaprima INT NOT NULL,
	quantidademateria INT NOT NULL,
	descricaoestoque VARCHAR(500),
	idproduto SMALLINT NOT NULL,
	CONSTRAINT PK_EstoqueMateriaPrima PRIMARY KEY (numeroestoquemateriaprima),
	FOREIGN KEY FK_EstoqueMateriaPrima(idproduto) REFERENCES Produto(idproduto)
);
#5
CREATE TABLE IF NOT EXISTS EstoqueProdutoFinal(
	numeroestoqueprodutofinal INT NOT NULL,
	quantidadeprodutofinal INT NOT NULL,
	descricaoestoque VARCHAR(500),
	idproduto SMALLINT NOT NULL,
	CONSTRAINT PK_EstoqueProdutoFinal PRIMARY KEY (numeroestoqueprodutofinal),
	FOREIGN KEY FK_EstoqueProdutoFinal(idproduto) REFERENCES Produto(idproduto)
);
#4
CREATE TABLE IF NOT EXISTS Produto(
	idproduto SMALLINT NOT NULL,
	descricaoproduto VARCHAR(500) NOT NULL,
  cnpj VARCHAR(14) NOT NULL,
	CONSTRAINT PK_Produto PRIMARY KEY (idproduto),
	CONSTRAINT FOREIGN KEY FK_Fornecedor(cnpj) REFERENCES Fornecedor(cnpj)
);
 #7
CREATE TABLE IF NOT EXISTS Cadastro(
	idcadastro SMALLINT NOT NULL,
	nivelseguranca SMALLINT NOT NULL,
	senha VARCHAR(50) NOT NULL,
	cnpj VARCHAR(14) NOT NULL,
	cpf VARCHAR(14) NOT NULL,
	CONSTRAINT PK_Cadastro PRIMARY KEY (idcadastro),
	FOREIGN KEY FK_Cadastro(cnpj) REFERENCES Fornecedor(cnpj),
	FOREIGN KEY FK_Cadastro2(cpf) REFERENCES Cliente(cpf)
);
