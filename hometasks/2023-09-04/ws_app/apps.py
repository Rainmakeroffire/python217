from django.apps import AppConfig


class WsAppConfig(AppConfig):
    name = 'ws_app'

    def ready(self):
        import ws_app.signals
