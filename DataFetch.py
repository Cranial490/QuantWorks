"""
DataFetch.py

Fetches historical candle data for instruments and writes into a csv file.
"""
from kiteconnect import KiteConnect
import Retriever
import os
from os import path
import csv
import util

def get_historical_records(configPath,access_token,instrument_token,start,end,timeframe):
    kite = util.setup_kite_instance(configPath,access_token)
    try:
        return kite.historical_data(instrument_token, start, end, timeframe)
    except Exception as e:
        print(e)


def write_to_csv(candleData, localPath, file_name):
    if path.exists(localPath):
        print("Directory already exists")
    else:
        os.mkdir(localPath)
    with open(path.join(localPath, file_name + '.csv'), 'w') as the_file:
        fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume']
        writer = csv.DictWriter(the_file, fieldnames=fieldnames)
        writer.writeheader()
        for line in candleData:
            writer.writerow(line)

def store_historical_data(configPath,dataPath,instrument_token,startDate,endDate,timeframe,instrument_name,file_name):
    config = util.fetch_config('./temp')
    access_token = util.get_config(config,'temp', 'access_token')
    records = get_historical_records(configPath,access_token,instrument_token,startDate, endDate,timeframe)
    if len(records) > 0:
        write_to_csv(records,path.join(dataPath,instrument_name),file_name)
    else:
        print("No data found for this date")

def main():
    configPath = '/Users/pp067807/Desktop/deleteLater/workSpace/dependencies/config.properties'
    dataPath = '/Users/pp067807/Desktop/deleteLater/workSpace/BackTestData'
    dates = util.get_dates(2016,1,1,2017,1,1)
    for day in dates:
        store_historical_data(configPath,dataPath,256265,day,day,'minute','NIFTY50',day)

if __name__ == '__main__':
    main()
