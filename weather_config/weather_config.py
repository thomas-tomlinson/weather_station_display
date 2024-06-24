import config

def default_config():
    #sane defaults
    config = {}
    config['weewx_host'] = 'weewx.local'
    return config

try:
    cfg = config.Config('weather.cfg') 
except FileNotFoundError as e:
    # config file wasn't found
    cfg = default_config()
