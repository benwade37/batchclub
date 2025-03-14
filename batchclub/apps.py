from django.apps import AppConfig


class BatchclubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'batchclub'

def ready(self):
    import users.signals
