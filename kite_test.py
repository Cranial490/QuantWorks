import logging
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker


logging.basicConfig(level=logging.DEBUG)

api_key = "lu3hm9qavt86o9uq"
api_secret="zdym5n8fpurc2a1jhlsrurjoksktuxtz"
request_token="D4bCIAzp6YdGCLLDScfLqKeeQ1rngtqh"
access_token = "iWJ28nyLEZXplrQStETDNicArKRQPHbL"

kite = KiteConnect(api_key=api_key)

order_id = 	kite.place_order(variety="regular", exchange="NSE", tradingsymbol="TATASTEEL", transaction_type="BUY", quantity=1, 
		product="MIS", order_type="LIMIT", price=446.00, trigger_price=445.00)
print(order_id)

#print(kite.positions())
#print(kite.orders())
#print(kite.instruments()) # returns list of ordered_dict 
#print(type(kite.instruments()))
#print(kite.login_url())
#print(kite.generate_session(request_token, api_secret))
'''
kws = KiteTicker(api_key, access_token)

def on_ticks(ws,ticks):
	#Callback to receive the ticks
	logging.debug("Ticks:{}".format(ticks))
	print("nigger")
	#Enter strategy here
	strategy()

def on_connect(ws,response):
	#suncribe to a list of instruments
	ws.subscribe([123,1231])
	#subscribe instrument
	ws.set_mode(ws.MODE_FULL,[123])

def on_close(ws,code,reason):
	#on connection close stop the main loop
	#reconnection will not happen after the execution of ws.stop()
	ws.stop()

def strategy():
	order_id = KiteConnect.place_order(variety="regular", exchange="NSE", tradingsymbol="TATASTEEL", transaction_type="BUY", quantity=1, 
		product="MIS", order_type="LIMIT", price=446.00, trigger_price=445.00)
	
	#pass

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
'''