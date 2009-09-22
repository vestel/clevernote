import ConfigParser
import os

config = ConfigParser.ConfigParser()
configfile = os.environ['HOME']+'/.clevernoterc'
config.read(configfile)

consumerKey = config.get('consumer', 'key')
consumerSecret = config.get('consumer', 'secret')

userStoreUri = config.get('server', 'uri')
noteStoreUriBase = config.get('server', 'base')

username = config.get('user', 'login')
password = config.get('user', 'passwd')

print(username)
