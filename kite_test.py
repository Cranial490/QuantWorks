#py -m pip install [package_name] on windows
import logging, csv
import pandas as pd
from datetime import datetime, date
import numpy as np
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
from datetime import date
import technical_indicators, Utilities, Globals


def on_ticks(ws,ticks):
	#Callback to receive the ticks
	global ohlc
	logging.debug("Ticks:{}".format(ticks))
	print("hello")
	#Enter strategy here
	interval = 5
	for tick in ticks:
		ohlc = Utilities.ticks_to_candle(self, tick, 5, ohlc)
	strategy()

def on_connect(ws,response):
	#suncribe to a list of instruments
	ws.subscribe([895745])
	#subscribe instrument
	ws.set_mode(ws.MODE_FULL,[895745])
	load_last_day_ticks()


def on_close(ws,code,reason):
	#on connection close stop the main loop
	#reconnection will not happen after the execution of ws.stop()
	write_to_csv()
	ws.stop()


def load_last_day_ticks():
	today = date.today()
	Globals.history_data_frame = pd.read_csv(str(today.day-1)+'.csv')
	Globals.history_data_frame.iloc[::-1]
	return Globals.history_data_frame



def write_to_csv():

	#print "DataFrame: ", Globals.data_frame
	# write dataframe to file at end of day
	time = datetime.now()
	today = str(date.today())
	if time.hour == 15 and time.minute == 30:
		Globals.data_frame.to_csv("./daily/"+today+'.csv', header=false, mode='a')



def strategy():
	order_id = kite.place_order(variety=kite.VARIETY_CO, exchange=kite.EXCHANGE_NSE, 
					tradingsymbol='TATASTEEL', transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=1, 
					product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_LIMIT, price=370, stoploss=368, 
					validity=kite.VALIDITY_DAY, disclosed_quantity=None,
                    squareoff=0)
	print("order_id = "+order_id)
	data = dict() #keeps extracted tick data

	for tick in ticks:
		token = tick["instrument_token"]
		ltp = tick["last_price"]
		volume = tick["volume"]
		timestamp = str(datetime.now().time())

		data[timestamp] = [token, ltp, volume]

	if(len(Globals.data_frame) == 0):
		Globals.data_frame.append(Globals.tick_df)
	else:
		Globals.data_frame = Globals.data_frame.append(Globals.tick_df) # append to existing

	
	df = Globals.data_frame[['LTP']]
	technical_indicators.sma(20)
	technical_indicators.ema(20)
	technical_indicators.ema_ema(20)
	technical_indicators.dema(20)
	technical_indicators.rsi(14)
	technical_indicators.vwap()
	technical_indicators.atr(ohlc, 14)
	



logging.basicConfig(level=logging.DEBUG)

# df_cols = ["Token", "LTP", "Volume"]
# Globals.data_frame = pd.DataFrame(data=[],columns=df_cols, index=[])
# Globals.tick_df = pd.DataFrame(data.values(), columns=df_cols, index=data.keys()) #convert data to a DataFrame
# Globals.history_data_frame = pd.DataFrame(data=[], columns=df_cols, index=[])

Globals.init()
ohlc = {}
for x in Globals.trd_portfolio:
	ohlc[x] = [0, 0, 0, 0, True, 300, 0]
api_key = "lu3hm9qavt86o9uq"
api_secret="zdym5n8fpurc2a1jhlsrurjoksktuxtz"
request_token="4qBpTP6DWXf3l4BiRkZlp5hsQY1UMkpj"
access_token = "LI6XmpR1RDQlhoRxtMBGiGpkVwQISqS7"

kite = KiteConnect(api_key=api_key)

kite.set_access_token(access_token)
#print(kite.instruments())

print(kite.positions())
#print(kite.orders())
#print(kite.instruments()) # returns list of ordered_dict 
kws = KiteTicker(api_key, access_token)

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
kws.connect()

