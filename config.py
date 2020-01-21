import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def get(key):
    splitkeys = key.split('#')
    if len(splitkeys) == 2:
        return config[splitkeys[0]][splitkeys[1]]
    else:
        raise Exception('check the config key')


get('weatherbit#accesskey')