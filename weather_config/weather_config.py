import json

cfg = {}
def default_config():
    #sane defaults
    def_cfg = {}
    def_cfg['weewx_host'] = 'weewx.local'
    def_cfg['sat_images'] = ['https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/GEOCOLOR/300x300.jpg']
    return def_cfg

def load_config():
    json_config = {}
    try:
        f = open('weather_cfg.json')
        
    except FileNotFoundError as e:
        return

    try:
        json_config = json.load(f)
        return json_config
    except Exception as e:
        return


config_file = load_config()
if config_file is not None:
    cfg = config_file
else:
    cfg = default_config()


