from configparser import ConfigParser
from quantworks import util
"""
Generates a config file at the provided path with provided parameter values
"""


def main():
    config = ConfigParser()

    config['login'] = {
        'username': 'default',
        'password': 'pass',
        'pin': '1234'
    }

    config['connection'] = {
        'api_key': 'apikeyishere',
        'api_secret': 'shhhitsasecret',
        'endpoint_url': 'https://kite.trade/connect/login?v=3&api_key=apikeyishere'
    }

    config['paths'] = {
        'chromeDriver': '/Users/akshaykhanna/Documents/testingQuantworks/chromeDriver/chromedriver'
    }
    localPath = './config.properties'
    util.write_config_file(localPath, 'w', config)


main()
