from configparser import ConfigParser
"""
Generates a config file at the provided path
"""
config = ConfigParser()

config['login'] = {
    'username': 'default',
    'password': 'pass',
    'pin': '1234'
}

config['connection'] = {
    'api_key': 'adsdnvsfo',
    'api_secret': 'shhhitsasecret',
    'endpoint_url': 'https://kite.trade/connect/login?v=3&api_key=api_key'
}

config['pahts'] = {
    'chromeDriver': '/Users/pp067807/Desktop/deleteLater/workSpace/dependencies/chromedriver'
}

localPath = './config.properties'
with open(localPath, 'w') as f:
    config.write(f)
