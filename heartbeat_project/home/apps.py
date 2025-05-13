from django.apps import AppConfig
import threading

class HomeConfig(AppConfig):
    name = 'home'

    def ready(self):
        from .hrm import connect_to_device
        import asyncio

        def run():
            try:
                asyncio.run(connect_to_device())  # ✅ اینجا coroutine اجرا میشه درست
            except Exception as e:
                print("❌ Error in BLE loop:", e)

        threading.Thread(target=run, daemon=True).start()
