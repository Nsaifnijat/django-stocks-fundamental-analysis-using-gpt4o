
from django.urls import path
from .consumers import StockPriceConsumer, GainersLossersConsumer

websocket_urlpatterns = [
        path('ws/stock_updates/', StockPriceConsumer.as_asgi()),
        path('ws/gainers_lossers_update/', GainersLossersConsumer.as_asgi()),

    ]
