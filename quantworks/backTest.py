import util
from os import listdir
from os.path import isfile, join

def initiate_backtest(dataPath,from_date,to_date):
    data_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    data_files.sort()

    for file in data_files:    
        candles = util.get_candles(dataPath,file,'5Min')
        strategy(candles)
        break
        
def strategy(candles):
    for key,value in candles.iterrows():
        print(value)
        break


mypath = '/Users/pp067807/Desktop/deleteLater/workSpace/BackTestData/DABUR'
initiate_backtest(mypath,'2016-01-9.csv','2016-01-12.csv')