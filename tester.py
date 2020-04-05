import os
from os import path
import csv


def main():
    print("starting write process")
    parentDir = "/Users/pp067807/Desktop/deleteLater/workSpace/BackTestData"
    instrument = "RELIANCE"
    localPath = path.join(parentDir, instrument)
    write_to_csv(record, localPath)


if __name__ == '__main__':
    print("triggering workflow")
    main()
