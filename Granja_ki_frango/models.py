from django.db import models

# Create your models here.

class Cliente(models.Model):

    nome = models.CharField(max_length=50, verbose_name="Nome")

    telefone = models.CharField(max_length=20, verbose_name="Telefone")

    def __str__(self):

        return self.nome

class Produto(models.Model):

    descricao = models.CharField(max_length=50, verbose_name="Descrição do Produto")

    def __str__(self):

        return self.descricao

class Pedido(models.Model):

    FORMA_PAGAMENTO_OPCOES = (

        ('PIX', 'Pix'),

        ('CARTAO', 'Cartão'),

        ('DINHEIRO', 'Dinheiro'),
        )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name="Produto")

    quantidade = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantidade")

    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Unitário")

    entregue = models.BooleanField(default=False, verbose_name="Entregue?")

    data_pedido = models.DateTimeField(auto_now_add=True, verbose_name="Data do Pedido")

    

    valor_recebido = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Valor Recebido")

    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO_OPCOES, null=True, blank=True, verbose_name="Forma de Pagamento")

    @property

    def valor_total(self):

        return self.quantidade * self.valor_unitario

    @property

    def saldo_restante(self):

        return self.valor_total - self.valor_recebido

    def __str__(self):

        return f"{self.cliente.nome} - {self.produto.descricao}"
