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


def setup_kite_instance(localPath):
    # get api_key from config file
    configParser = util.fetch_config()
    api_key = util.get_config(configParser,'connection','api_key')
    kite = KiteConnect(api_key=api_key)
    access_token = Retriever.getAccessToken()
    try:
        kite.set_access_token(access_token)
    except Exception as e:
        print(e, "Error while setting access token")
    return kite


def get_historical_records():
    kite = setup_kite_instance()
    try:
        return kite.historical_data(3821313, '2019-12-04', '2019-12-04', 'minute')
    except Exception as e:
        print(e)

def write_to_csv(candleData, localPath, instrument):
    if path.exists(localPath):
        print("Directory already exists")
    else:
        os.mkdir(localPath)
    with open(path.join(localPath, instrument + '.csv'), 'w') as the_file:
        fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume']
        writer = csv.DictWriter(the_file, fieldnames=fieldnames)
        writer.writeheader()
        for line in candleData:
            writer.writerow(line)

def main():
    print("fetching records ....")
    records = get_historical_records()
    # print(records)
    # write_to_csv(records)
    parentDir = "/Users/pp067807/Desktop/deleteLater/workSpace/BackTestData"
    instrument = "RELIANCE"
    localPath = os.path.join(parentDir, instrument)
    write_to_csv(records, localPath, instrument)


if __name__ == '__main__':
    main()
