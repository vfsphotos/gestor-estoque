from django.db import models


class Fornecedor(models.Model):
    razao_social = models.CharField(
        max_length=100,
        verbose_name='Razão social do fornecedor',
        unique=True
    )
    nome_fantasia = models.CharField(
        max_length=100,
        verbose_name='Nome fantasia do fornecedor'
    )
    produtos = models.ManyToManyField(
        'produto.Produto',
        verbose_name='Produtos fornecedor',
        through='FornecedorProduto',
        through_fields=('Fornecedor', 'Produto')
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='data de criação do fornecedor'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True, 
        verbose_name='data de atualização do fornecedor'
    )
    
    class Meta:
        tb_table = 'fornecedores'

class FornecedorProduto(models.Model):
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.CASCADE,
        verbose_name='Fornecedor do produto'
    )
    produto = models.ForeignKey(
        'produtos.Produto',
        on_delete=models.CASCADE,
        verbose_name='Produto do fornecedor'
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Preço do produto'
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='data de criação'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True, 
        verbose_name='data de atualização'
    )
    class Meta:
        tb_table = 'fornecedor_produto'

class Produto(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name='nome do produto'
    )
    categoria = models.ForeignKey(
        'produtos.Categoria',
        on_delete=models.CASCADE,
        verbose_name='categoria do produto'
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='data de criação do produto'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True, 
        verbose_name='data de atualização do produto'
    )

    class Meta:
        tb_table = 'produtos'

class Categoria(models.Model):
    nome = models.CharField(
        max_length=100, 
        verbose_name='nome da categoria',
        unique=True
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='data de criação da categoria'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True, 
        verbose_name='data de atualização da categoria'
    )

    class Meta:
        tb_table = 'categorias'


