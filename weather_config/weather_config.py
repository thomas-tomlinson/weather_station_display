import config

def default_config():
    #sane defaults
    config = {}
    config['weewx_host'] = 'weewx.local'
    config['sat_images'] = ['https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/GEOCOLOR/300x300.jpg']
    return config

try:
    cfg = config.Config('weather.cfg') 
except FileNotFoundError as e:
    # config file wasn't found
    cfg = default_config()
