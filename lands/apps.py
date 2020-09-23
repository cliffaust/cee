from django.apps import AppConfig


class LandsConfig(AppConfig):
    name = "lands"

    def ready(self):
        import lands.signals
