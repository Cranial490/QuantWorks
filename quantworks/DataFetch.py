"""
DataFetch.py

Fetches historical candle data for instruments and writes into a csv file.
"""
import os
from os import path
import csv
from quantworks import util

"""
fetches historical candle data from kite server, return list of candles
"""


def get_historical_records(configPath, access_token, instrument_token, start, end, timeframe, continuous=False, oi=False):
    kite = util.setup_kite_instance(configPath, access_token)
    try:
        return kite.historical_data(instrument_token, start, end, timeframe, continuous=continuous, oi=oi)
    except Exception as e:
        print(e)


"""
writes the data to csv files
"""


def write_to_csv(candleData, localPath, file_name):
    if path.exists(localPath):
        pass
    else:
        print("creating directory: " + localPath)
        os.mkdir(localPath)
    with open(path.join(localPath, file_name + '.csv'), 'w') as the_file:
        fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'oi']
        writer = csv.DictWriter(the_file, fieldnames=fieldnames)
        writer.writeheader()
        for line in candleData:
            writer.writerow(line)


"""
helper for writing data to csv
"""


def store_historical_data(configPath, dataPath, instrument_token, startDate, endDate, timeframe, instrument_name, file_name, continuous=False, oi=False):
    config = util.fetch_config('./temp')
    access_token = util.get_config(config, 'temp', 'access_token')
    records = get_historical_records(
        configPath, access_token, instrument_token, startDate, endDate, timeframe, continuous, oi)
    if records != None:
        if len(records) > 0:
            write_to_csv(records, path.join(
                dataPath, instrument_name), file_name)
        else:
            print("No data found for this date: " + startDate)

    else:
        print("returned None for date: " + startDate)


def main():
    configPath = '/Users/akshaykhanna/Documents/QuantWorks/config.properties'
    dataPath = '/Users/akshaykhanna/Documents/testingQuantworks/BackTestData'

    dates = util.get_dates(2020, 3, 15, 2020, 4, 10)
    for day in dates:
        store_historical_data(configPath, dataPath, 14351106,
                              day, day, 'minute', 'NIFTY', day)


if __name__ == '__main__':
    main()
