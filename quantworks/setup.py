"""
setup.py - fetches access token from kite and list of intruments for specified exchange
"""
from quantworks import Retriever
from quantworks import util
from configparser import ConfigParser
from os import path
import csv


def write_dict_to_csv(data):
    fieldnames = ['instrument_token', 'exchange_token', 'tradingsymbol', 'name', 'last_price',
                  'expiry', 'strike', 'tick_size', 'lot_size', 'instrument_type', 'segment', 'exchange']

    with open('./INSTRUMENTS.csv', 'w') as f:
        writer = csv.DictWriter(f, delimiter=",", fieldnames=fieldnames)
        writer.writeheader()
        for line in data:
            writer.writerow(line)


def main():
    configPath = '/Users/akshaykhanna/Documents/QuantWorks/quantworks/config.properties'
    exchange = 'NSE'
    # checking if access token in local else fetching from api
    if path.exists('./temp') == False:
        access_token = Retriever.getAccessToken(configPath)
        config = ConfigParser()
        config['temp'] = {
            'access_token': access_token
        }
        util.write_config_file('./temp', 'w', config)

    # fetching access token
    config = util.fetch_config('./temp')
    access_token = util.get_config(config, 'temp', 'access_token')

    # initializing kite
    kite = util.setup_kite_instance(configPath, access_token)

    # fetching instruments list
    instrument_list = kite.instruments(exchange=exchange)

    write_dict_to_csv(instrument_list)


main()
