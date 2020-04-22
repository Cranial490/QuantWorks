import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

api_key = ""
access_token = ""

kws = KiteTicker(api_key, access_token)

def on_ticks(ws,ticks):
	#Callback to receive the ticks
	logging.debug("Ticks:{}".format(ticks))
	#Enter strategy here

def on_connect(ws,response):
	#suncribe to a list of instruments
	ws.subscribe([123,1231])
	#subscribe instrument
	ws.set_mode(ws.MODE_FULL,[123])

def on_close(ws,code,reason):
	#on connection close stop the main loop
	#reconnection will not happen after the execution of ws.stop()
	ws.stop()

def on_message()

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
