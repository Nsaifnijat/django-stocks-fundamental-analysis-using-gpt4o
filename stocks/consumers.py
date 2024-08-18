# stocks/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StockPriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'stock_updates'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def update_stock_price(self, event):
        price = event['price']

        # Send stock price update to WebSocket
        await self.send(text_data=json.dumps({
            'price': price
        }))
class GainersLossersConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'gainers_lossers_update'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def daily_gainers_and_lossers(self, event):
        gainers = event['gainers']
        lossers = event['lossers']

        await self.send( text_data= json.dumps(
            {
                'gainers': gainers,
                'lossers': lossers
            }
        ))