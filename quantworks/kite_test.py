import logging, csv
import pandas as pd
from datetime import datetime, date
import numpy as np
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker


logging.basicConfig(level=logging.DEBUG)

api_key = "lu3hm9qavt86o9uq"
api_secret="zdym5n8fpurc2a1jhlsrurjoksktuxtz"
request_token="PmxdHe7ZZd1O3jhsEJ3y1WuenOEhg5PO"
access_token = "TU5tHhaU3aDvQ4TTMgplUaJN3IndQYX8"

kite = KiteConnect(api_key=api_key)



#order_id = 	kite.place_order(variety="regular", exchange="NSE", tradingsymbol="TATASTEEL", transaction_type="BUY", quantity=1, 
#		product="MIS", order_type="LIMIT", price=446.00, trigger_price=445.00)
#print(order_id)


#print(kite.login_url())
#print(kite.generate_session(request_token, api_secret))
#print(kite.instruments())

#print(kite.positions())
#print(kite.orders())
#print(kite.instruments()) # returns list of ordered_dict 


df_cols = ["Token", "LTP", "Volume"]

data_frame = pd.DataFrame(data=[],columns=df_cols, index=[])

kws = KiteTicker(api_key, access_token)

def on_ticks(ws,ticks):
	#Callback to receive the ticks
	logging.debug("Ticks:{}".format(ticks))
	print("nigger")
	# writing tick data to dataframes
	'''
	global data_frame, df_cols

	data = dict() #keeps extracted tick data

	for tick in ticks:
		token = tick["instrument_token"]
		ltp = tick["last_price"]
		volume = tick["volume"]
		timestamp = str(datetime.now().time())

		data[timestamp] = [token, ltp, volume]

	tick_df = pd.DataFrame(data.values(), columns=df_cols, index=data.keys()) #convert data to a DataFrame
	if(len(data_frame) == 0):
		data_frame.append(tick_df)
	else:
		data_frame = data_frame.append(tick_df) # append to existing

	#print "DataFrame: ", data_frame
	# write dataframe to file at end of day
	time = datetime.now()
	today = str(date.today())
	if time.hour == 15 and time.minute == 30:
		data_frame.to_csv("./daily/"+today+'.csv', header=false, mode='a')
	'''
	#Enter strategy here
	strategy()

def on_connect(ws,response):
	#suncribe to a list of instruments
	ws.subscribe([895745])
	#subscribe instrument
	ws.set_mode(ws.MODE_FULL,[895745])

def on_close(ws,code,reason):
	#on connection close stop the main loop
	#reconnection will not happen after the execution of ws.stop()
	ws.stop()

def strategy():
	order_id = kite.place_order(variety=kite.VARIETY_CO, exchange=kite.EXCHANGE_NSE, 
					tradingsymbol='TATASTEEL', transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=1, 
					product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_LIMIT, price=428, stoploss=425.5, 
					validity=kite.VALIDITY_DAY, disclosed_quantity=None,
                    squareoff=0)
	print(order_id)
	
#order = kite.place_order(variety=kite.VARIETY_CO ,exchange=kite.EXCHANGE_MCX, 
#	tradingsymbol = 'CRUDEOIL JUN FUT',transaction_type = kite.TRANSACTION_TYPE_BUY, 
#	quantity = 1, product=kite.PRODUCT_MIS, stoploss = 3610, price=3665, order_type=kite.ORDER_TYPE_LIMIT, 
#	validity = kite.VALIDITY_DAY, disclosed_quantity = None, squareoff = 0 ) 

	'''
	global data_frame, df_cols
	df = data_frame[["LTP"]]
	df.reset_index(level=0, inplace=True)
	df.columns = ['ds', 'y']
	ma20 = df.y.rolling(window=20).mean()
	ma50 = df.y.rolling(window=50).mean()
	exp20 = df.y.ewm(span=20, min_periods=20, adjust=False).mean()
	exp50 = df.y.ewm(span=50, min_periods=50, adjust=False).mean()
	'''
	
	
	#pass




kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
kws.connect()

