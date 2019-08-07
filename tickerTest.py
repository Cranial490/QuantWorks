import logging, csv
import pandas as pd
from datetime import datetime, date
import numpy as np
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker


logging.basicConfig(level=logging.DEBUG)

api_key = "lu3hm9qavt86o9uq"
api_secret="zdym5n8fpurc2a1jhlsrurjoksktuxtz"
request_token="imGpoAdnaC1ysZv3Zdn3Yly6dcZVEjug"
access_token = "DIf8Ieq3waWnBVDYFpIgIDpDZklo5GGN"

kite = KiteConnect(api_key=api_key)

# data = kite.generate_session(request_token, api_secret)
kite.set_access_token(access_token)
kws = KiteTicker(api_key,access_token)

def on_ticks(ws, ticks):
    # Callback to receive ticks.
    logging.debug("Ticks: {}".format(ticks))
    print(kite.positions())

def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([1246721])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [1246721])

def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()