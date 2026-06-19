from django.contrib import admin
from django.db.models import Sum
from .models import Cliente, Produto, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    # Campos que aparecem na lista
    list_display = ('cliente', 'produto', 'quantidade', 'valor_total', 'entregue', 'data_pedido')
    
    # Filtros na lateral direita
    list_filter = ('produto', 'entregue', 'data_pedido')
    
    # Campo de busca
    search_fields = ('cliente__nome', 'produto__descricao')

    # Mágica para somar o total de quilos (quantidade)
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        
        try:
            # Pega o queryset que já está filtrado na tela
            qs = response.context_data['cl'].queryset
            
            # Soma a 'quantidade' de todos os itens filtrados
            soma_total = qs.aggregate(total=Sum('quantidade'))['total'] or 0
            
            # Adiciona ao contexto para exibir no template
            response.context_data['total_quantidade'] = soma_total
        except (AttributeError, KeyError):
            pass
            
        return response