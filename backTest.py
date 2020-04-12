import util
from os import listdir
from os.path import isfile, join

def initiate_backtest(dataPath,from_date,to_date):
    data_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    data_files.sort()
    for file in data_files:
        from_date = from_date + '.csv'
        if (file > from_date) and (file < to_date):
            #read data from csv and store in some format
            #add strategy for backtesting here 
            print('reading file' + file)
mypath = '/Users/pp067807/Desktop/deleteLater/workSpace/BackTestData/DABUR'
