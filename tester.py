import os
from os import path
import csv
import util
import Retriever
import util


def main():
    print("starting write process")
    os.environ["ACCESSTOKEN"] = "tricklw"
    # print(Retriever.getAccessToken())


if __name__ == '__main__':
    # print("triggering workflow")
    # localPath = '/Users/pp067807/Desktop/deleteLater/workSpace/dependencies/config.properties'
    # parser = util.fetch_config(localPath)
    # print(util.get_config(parser, 'paths', 'dataPath'))
    main()
