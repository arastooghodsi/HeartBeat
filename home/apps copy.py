from django.apps import AppConfig
import threading

class HomeConfig(AppConfig):
    name = 'home'

    def ready(self):
        from . import hrm
        thread = threading.Thread(target=hrm.run_heartbeat_simulator, daemon=True)
        thread.start()
