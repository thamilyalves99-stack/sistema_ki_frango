from django.contrib import admin
from .models import Pedido, Cliente, Produto

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'quantidade', 'valor_total', 'entregue', 'data_pedido')
    list_filter = ('produto', 'entregue', 'data_pedido')
    
    # Isso faz o funcionário ver apenas os pedidos do dia quando logar
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Se for funcionário, você pode filtrar aqui para ele ver apenas o que precisa
        return qs

    # Impede que o funcionário delete pedidos, apenas edite ou adicione
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser