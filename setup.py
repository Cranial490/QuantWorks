import Retriever
import util
from configparser import ConfigParser
from kiteconnect import KiteConnect
from os import path
import csv


def write_dict_to_csv(fieldnames,data):
    with open('./INSTRUMENTS.csv', 'w') as f:
        writer = csv.DictWriter(f,delimiter=",",fieldnames=fieldnames)
        writer.writeheader()
        for line in data:
            writer.writerow(line)

def main():
    configPath = '/Users/pp067807/Desktop/deleteLater/workSpace/dependencies/config.properties'
    if path.exists('./temp') == False:
        access_token = Retriever.getAccessToken(configPath)
        config = ConfigParser()
        config['temp'] = {
           'access_token': access_token
         }
        util.write_config_file('./temp', 'w', config)
    config = util.fetch_config('./temp')
    access_token = util.get_config(config,'temp', 'access_token')
    kite = util.setup_kite_instance(configPath, access_token)
    instrument_list = kite.instruments(exchange = 'NSE')
    fieldnames = ['instrument_token','exchange_token','tradingsymbol','name','last_price','expiry','strike','tick_size','lot_size','instrument_type','segment','exchange']
    write_dict_to_csv(fieldnames,instrument_list)

main()
