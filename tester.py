import os
from os import path
import csv
import util


def main():
    print("starting write process")


if __name__ == '__main__':
    print("triggering workflow")
    localPath = '/Users/pp067807/Desktop/deleteLater/workSpace/dependencies/config.properties'
    parser = util.fetch_config(localPath)
    print(util.get_config(parser, 'login', 'username'))
    main()
