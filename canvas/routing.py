from django.urls import re_path
from skechwime.consumers import CanvasConsumer

websocket_urlpatterns = [
    re_path(r'ws/canvas/(?P<lobby_name>\w+)/$', CanvasConsumer.as_asgi()),
]
