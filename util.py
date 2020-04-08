from configparser import ConfigParser

"""
Reads config file from the localPath.

params:
localPath - path of configuration file.
"""


def fetch_config(localPath):
    parser = ConfigParser()
    parser.read(localPath)
    return parser


"""
returns the config parameters.
params:
parser - object containing the config parameters.
section - section of config file.
key - parameter to be fetched.
"""


def get_config(parser, section, key):
    return parser.get(section, key)


"""
writes to configuration file specified in path
params:
parser - object containing the config parameters.
specifier - read,write,append ('w','r','a' etc.)
localPath - path to the configuration file
"""


def write_config_file(localPath, specifier, config):
    with open(localPath, specifier) as f:
        config.write(f)
