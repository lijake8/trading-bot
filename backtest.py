import alpaca_trade_api as tradeapi
import numpy as np
import time
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

SEC_KEY = '9Ke6K5JVuWBEGLq3Fudz0wP0cE7wjyerO09zvoDL' # Enter Your Secret Key Here
PUB_KEY = 'PKO29S6OJ4436FHMWTGM' # Enter Your Public Key Here
BASE_URL = 'https://paper-api.alpaca.markets' # This is the base URL for paper trading
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)
# print(api)

symb = "SPY"
pos_held = False
hours_to_test = 2



# data = api.get_bars("AAPL", tradeapi.TimeFrame(4, tradeapi.TimeFrameUnit.Hour), start="2022-05-01", adjustment='raw') #4-hour time frame data
data = api.get_bars(symb, tradeapi.TimeFrame(1, tradeapi.TimeFrameUnit.Minute), start="2022-05-01", adjustment='raw')

data_dataframe = data.df
# print(data_dataframe)
# print(data)
# print(type(data_dataframe))
print(type(data))
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')










print("Checking Price")
# market_data = api.get_barset(symb, 'minute', limit=(60 * hours_to_test)) # Pull market data from the past 60x minutes
market_data = data

close_list = []
for bar in market_data:
    # print(bar)
    close_list.append(bar.c)



print("Open: " + str(close_list[0]))
print("Close: " + str(close_list[60 * hours_to_test - 1]))


close_list = np.array(close_list, dtype=np.float64)
startBal = 2000 # Start out with 2000 dollars
balance = startBal
buys = 0
sells = 0



for i in range(4, 60 * hours_to_test): # Start four minutes in, so that MA can be calculated
    ma = np.mean(close_list[i-4:i+1])
    last_price = close_list[i]

    print("Moving Average: " + str(ma))
    print("Last Price: " + str(last_price))

    if ma + 0.1 < last_price and not pos_held:
        print("Buy")
        balance -= last_price
        pos_held = True
        buys += 1
    elif ma - 0.1 > last_price and pos_held:
        print("Sell")
        balance += last_price
        pos_held = False
        sells += 1
    print(balance)
    time.sleep(0.01)

print("")
print("Buys: " + str(buys))
print("Sells: " + str(sells))

if buys > sells:
    balance += close_list[60 * hours_to_test - 1] # Add back your equity to your balance
    

print("Final Balance: " + str(balance))

print("Profit if held: " + str(close_list[60 * hours_to_test - 1] - close_list[0]))
print("Profit from algorithm: " + str(balance - startBal))