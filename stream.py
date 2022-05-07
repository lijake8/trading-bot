from alpaca_trade_api.stream import Stream

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)
    
async def bar_callback(b):
    print('bar', b)

SEC_KEY = '9Ke6K5JVuWBEGLq3Fudz0wP0cE7wjyerO09zvoDL' # Enter Your Secret Key Here
PUB_KEY = 'PKO29S6OJ4436FHMWTGM' # Enter Your Public Key Here
BASE_URL = 'https://paper-api.alpaca.markets' # This is the base URL for paper trading
# Initiate Class Instance
stream = Stream(key_id= PUB_KEY, 
                secret_key=SEC_KEY, 
                base_url=BASE_URL,
                data_feed='iex',
                websocket_params =  {'ping_interval': 5}, #here we set ping_interval to 5 seconds 
                )

# subscribing to event
# stream.subscribe_trades(trade_callback, 'AAPL')
# stream.subscribe_quotes(quote_callback, 'IBM')
stream.subscribe_bars(bar_callback, 'SPY')

stream.run()