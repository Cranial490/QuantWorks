import logging, csv
import pandas as pd
from datetime import datetime, date
import numpy as np
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker

def tokenList(kite):
	return kite.instruments()

logging.basicConfig(level=logging.DEBUG)

api_key = "lu3hm9qavt86o9uq"

api_secret="zdym5n8fpurc2a1jhlsrurjoksktuxtz"

#fetch the new requent token from the url and paste here.
request_token="1LY6KD20gTwur9OSdfnf0lX3IMU9dLlQ"

kite = KiteConnect(api_key=api_key)

data = kite.generate_session(request_token, api_secret)

print("access_token: ",data["access_token"])