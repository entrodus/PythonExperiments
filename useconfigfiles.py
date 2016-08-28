#https://docs.python.org/3/library/configparser.html
import configparser
config = configparser.ConfigParser()
config.read('useconfigfiles.ini')


print(config['SETTINGS']['name'])
print(config['OTHERSETTINGS']['othersetting'])