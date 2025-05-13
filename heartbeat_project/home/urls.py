from django.urls import path
from .views import live_heartbeat_view

urlpatterns = [
    path('live/', live_heartbeat_view, name='live_heartbeat'),
]
