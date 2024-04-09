from django.apps import AppConfig

class TicketingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jo2024'

    def ready(self):
        # Importer l'application users
        import users