from kiteconnect import KiteConnect
import Retriever
import os
from os import path
import csv


def setup_kite_instance():
    # get api_key from config file
    api_key = "irtkrxee8bs6fecn"
    kite = KiteConnect(api_key=api_key)
    access_token = Retriever.getAccessToken()
    try:
        kite.set_access_token(access_token)
    except Exception as e:
        print(e, "Error while setting access token")
    return kite

# fetching historical data


def get_historical_records():
    kite = setup_kite_instance()
    try:
        return kite.historical_data(3821313, '2019-12-04', '2019-12-04', 'minute')
    except Exception as e:
        print(e)


# def write_to_csv(candleData):
#     with open(path.join(args.path, name + '.csv'), 'w') as the_file:
#         fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'oi']
#         writer = csv.DictWriter(the_file, fieldnames=fieldnames)
#         writer.writeheader()
#         for line in candleData:
#             writer.writerow(line)
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
