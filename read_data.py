import alpaca_trade_api as tradeapi
import numpy as np
import time

from buy_sell import BASE_URL, PUB_KEY, SEC_KEY

# SEC_KEY = ''
# PUB_KEY = ''
# BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)

symb = "SPY"

while True:
    print("")
    print("Checking Price")
    
    market_data = api.get_barset(symb, 'minute', limit=5) # Get one bar object for each of the past 5 minutes

    close_list = [] # This array will store all the closing prices from the last 5 minutes
    for bar in market_data[symb]:
        close_list.append(bar.c) # bar.c is the closing price of that bar's time interval

    close_list = np.array(close_list, dtype=np.float64) # Convert to numpy array
    ma = np.mean(close_list)
    last_price = close_list[4] # Most recent closing price

    print("Moving Average: " + str(ma))
    print("Last Price: " + str(last_price))
    
    time.sleep(60) # Wait one minute before retreiving more market data