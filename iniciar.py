import os
import django
from django.core.management import call_command

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_ki_frango.settings')
django.setup()

# Tenta aplicar as migrações
try:
    print("A executar migrações...")
    call_command('migrate', '--noinput')
    print("Migrações concluídas com sucesso!")
except Exception as e:
    print(f"Erro ao migrar: {e}")