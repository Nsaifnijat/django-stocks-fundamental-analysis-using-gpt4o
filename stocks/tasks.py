
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Stock
import yfinance as yf
import json
from random import randint

#import robin_stocks.robinhood as rh
import time
import math
#robin = rh.authentication.login('vvvvv@gmail.com', 'vvv@gggg')



@shared_task
def fetch_stock_price():
    symbol = 'AAPL'
    stock = yf.Ticker(symbol)
    
    # Fetching the latest price
    latest_price = stock.history(period='1d')['Close'].iloc[-1]
    print('this is latest price:', latest_price)
    
    # Save the stock data to the database
    Stock.objects.create(symbol=symbol, price=latest_price)
    
    
    latest_price = randint(0,500) # COMMENT THIS LINE, right now its just for demonstration.
    # Broadcast the updated stock price to WebSocket clients
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'stock_updates',
        {
            'type': 'update_stock_price',
            'price': latest_price
        }
    )    
    return f'Stock price for {symbol} updated to {latest_price}'




# Function to calculate percent gain
def calculate_percent_gain(last_trade_price, previous_close):
    return ((last_trade_price - previous_close) / previous_close) * 100




"""
#ignore this commented code!

@shared_task
def fetch_top_gainers_lossers():
    abov_five_percent_gain = {}
    below_five_percent_loss = {}
    percent_range = 0.4 #0.25 on spy @550

    top = rh.markets.get_top_movers()
    # Process the data
    for stock in top:
        
        symbol = stock['symbol']
        last_trade_price = float(stock['last_trade_price'])
        previous_close = float(stock['adjusted_previous_close'])
        percent_gain = calculate_percent_gain(last_trade_price, previous_close)
        #if price = 550, range=0.25. range would be 0.04 percent of price. to find range from percent
        range = last_trade_price * (percent_range/100)
        capital = 200
        #ADDING only five percent gainers to the loop
        if percent_gain > 5:
            buy_1 = math.ceil(capital/float(last_trade_price))
            buy_3 = 3 * buy_1
            abov_five_percent_gain[symbol] = { "price": last_trade_price, "range" : range , "gain": percent_gain, 'buy_1' : buy_1, 'buy_3': buy_3 }
            
        elif percent_gain < -5:
            buy_1 = math.ceil(capital/float(last_trade_price))
            buy_3 = 3 * buy_1
            below_five_percent_loss[symbol] = { "price": last_trade_price, "range" : range , "gain": percent_gain, 'buy_1': buy_1, 'buy_3': buy_3 }
        else:
            if symbol in abov_five_percent_gain:
                del abov_five_percent_gain[symbol]
            elif symbol in below_five_percent_loss:
                del below_five_percent_loss[symbol]
    with open('gainers.json','w') as f:
                json.dump(abov_five_percent_gain, f)
    with open('lossers.json', 'w') as f:
                json.dump(below_five_percent_loss, f)
    # Broadcast the updated stock price to WebSocket clients
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'gainers_lossers_update',
        {
            'type': 'daily_gainers_and_lossers',
            'gainers': abov_five_percent_gain,

            'lossers': below_five_percent_loss,
        }
    )    
    print(abov_five_percent_gain)
    #return f'todays gainers are {abov_five_percent_gain.keys()} and lossers are { below_five_percent_loss.keys()}'
"""