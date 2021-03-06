# in routing.py
from channels.routing import route
from .consumers import ws_connect, ws_message, ws_disconnect


websocket_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]