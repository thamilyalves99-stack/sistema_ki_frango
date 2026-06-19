from django.contrib import admin
from .models import Cliente, Produto, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'quantidade', 'valor_total', 'entregue', 'data_pedido')
    list_filter = ('entregue', 'forma_pagamento', 'data_pedido')
    search_fields = ('cliente__nome', 'produto__descricao')