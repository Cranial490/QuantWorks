from configparser import ConfigParser
import util
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

    config['pahts'] = {
        'chromeDriver': '/Users/pp067807/Desktop/deleteLater/workSpace/dependencies/chromedriver'
    }
    localPath = './config.properties'
    util.write_config_file(localPath, 'w', config)


main()
