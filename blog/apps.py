from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    """
    Provides primary key type for blog app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
