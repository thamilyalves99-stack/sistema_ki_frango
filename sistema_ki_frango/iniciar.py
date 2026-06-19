import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_ki_frango.settings')
django.setup()
call_command('migrate')
print("Banco de dados criado com sucesso!")