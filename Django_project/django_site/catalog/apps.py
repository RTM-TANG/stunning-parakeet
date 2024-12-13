from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """Configuration options for the application are set in this class

    Args:
        AppConfig (AppConfig): Represent a Django app and its configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
