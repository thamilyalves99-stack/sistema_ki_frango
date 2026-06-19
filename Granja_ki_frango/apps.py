from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

class GranjaKiFrangoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Granja_ki_frango'

    def ready(self):
        try:
            User = get_user_model()
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@ki-frango.com', '123456')
        except OperationalError:
            pass # A tabela ainda não existe, o migrate vai tratar disso