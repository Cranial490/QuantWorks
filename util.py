"""
contains all the helper methods
"""
from configparser import ConfigParser
import csv
from kiteconnect import KiteConnect
from datetime import date, timedelta
import pandas as pd
import os
"""
Reads config file from the localPath.

params:
localPath - path of configuration file.
"""


def fetch_config(configPath):
    parser = ConfigParser()
    parser.read(configPath)
    return parser


"""
returns the config parameters.
params:
parser - object containing the config parameters.
section - section of config file.
key - parameter to be fetched.
"""


def get_config(parser, section, key):
    return parser.get(section, key)


"""
writes to configuration file specified in path
params:
parser - object containing the config parameters.
specifier - read,write,append ('w','r','a' etc.)
localPath - path to the configuration file
"""


def write_config_file(configPath, specifier, config):
    with open(configPath, specifier) as f:
        config.write(f)


"""
returns kite instance
params:
configPath - path for configuration file
access_token - access token for kite api
"""


def setup_kite_instance(configPath, access_token):
    configParser = fetch_config(configPath)
    api_key = get_config(configParser, 'connection', 'api_key')
    kite = KiteConnect(api_key=api_key)
    access_token = access_token
    try:
        kite.set_access_token(access_token)
    except Exception as e:
        print(e, "Error while setting access token")
    return kite


"""
returns a list of dates between two dates
params:
s_year - start year
s_month - start month
s_date - start date
e_year - end year
e_month - end month
e_date - end date
"""


def get_dates(s_year, s_month, s_date, e_year, e_month, e_date):
    startDate = date(s_year, s_month, s_date)
    endDate = date(e_year, e_month, e_date)
    delta = endDate - startDate
    date_list = []
    for i in range(delta.days + 1):
        day = startDate + timedelta(days=i)
        date_list.append(day.strftime("%Y-%m-%d"))
    return date_list


"""
returns dataframe containing ohlc candle data according to the specified timeframe

params:
dataPath - path to the folder containing .csv data
date - date for which data need to be fetched
timeframe - timeframe for a candle e.g 1Min, 5Min, .... 
"""


def get_candles(dataPath, file_name, timeframe):
    filePath = os.path.join(dataPath, file_name)
    df = pd.read_csv(filePath)
    df = df.set_index(pd.to_datetime(df['date']))
    if timeframe != '1Min':
        df = df.resample(timeframe).agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum',
            'oi': 'sum'
        })

    return df
