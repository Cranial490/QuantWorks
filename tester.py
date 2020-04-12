import util
import pandas as pd
import os
mypath = '/Users/pp067807/Desktop/deleteLater/workSpace/BackTestData/DABUR'
file_name = '2016-01-20'
# df = pd.read_csv(mypath)
# df = pd.read_csv(mypath)
# # df.info()
# df = df.set_index(pd.to_datetime(df['date']))
# # df['date'] = pd.to_datetime(df['date']).astype('datetime64[ns]')
# # print(df.index)
# df = df.resample('5Min').agg({
#     'open':'first',
#     'high':'max',
#     'low':'min',
#     'close':'last',
#     'volume': 'sum'
# })

# print(df)

def get_candles(dataPath,date,timeframe):
    
    filePath = os.path.join(dataPath,date + '.csv')
    df = pd.read_csv(filePath)
    df = df.set_index(pd.to_datetime(df['date']))
    if timeframe !='1Min':
        df = df.resample(timeframe).agg({
        'open':'first',
        'high':'max',
        'low':'min',
        'close':'last',
        'volume': 'sum',
        'oi': 'sum'
        })

    return df


print(get_candles(mypath,file_name,'15Min'))

