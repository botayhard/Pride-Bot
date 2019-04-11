"""This module is used for reading configuration"""

import configparser
from os import environ

class Configuration:
    def __init__(self):
        self.token = ''

def load_configuration(file_name='config'):
    """Load configuration from file"""
    config = Configuration()
    parser = configparser.ConfigParser()
    parser.read(file_name)
    default_section = parser['DEFAULT']
    config.token = environ.get('BOT_TOKEN', default_section['token'])
    return config
