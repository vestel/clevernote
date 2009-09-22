import ConfigParser
import os
import sys

config = ConfigParser.ConfigParser()
configfile = os.environ['HOME']+'/.clevernoterc'
config.read(configfile)

newConfig = ConfigParser.ConfigParser()

consumerKey = config.get('consumer', 'key')
consumerSecret = config.get('consumer', 'secret')

userStoreUri = config.get('server', 'uri')
noteStoreUriBase = config.get('server', 'base')

username = config.get('user', 'login')
password = config.get('user', 'passwd')

if len(sys.argv) < 2:
    print "Arguments:  %s <key> <value>" % sys.argv[0]
    print "Use '%s help' for more info"  % sys.argv[0]
    exit(1)

key = sys.argv[1]

if (key == 'help'):
    print "Arguments:  %s <key> <value>" % sys.argv[0]
    help = """Keys are: 
        secret: 
        key:
        login:
        passwd:
        uri:
        base:
    """
    print(help)
    exit(0)

value = sys.argv[2]

newConfig.add_section('consumer')
if (key == 'key'):
    newConfig.set('consumer', 'key', value)
else:
    newConfig.set('consumer', 'key', consumerKey)        

if (key == 'secret'):
    newConfig.set('consumer', 'secret', value)
else:
    newConfig.set('consumer', 'secret', consumerSecret)        

newConfig.add_section('user')
if (key == 'passwd'):
    newConfig.set('user', 'passwd', value)
else:
    newConfig.set('user', 'passwd', password)
if (key == 'login'):
    newConfig.set('user', 'login', value) 
else:
    newConfig.set('user', 'login', username)

newConfig.add_section('server')
if (key == 'base'):
    newConfig.set('server', 'base', value)
else:
    newConfig.set('server', 'base', noteStoreUriBase)
if (key == 'uri'):
    newConfig.set('server', 'uri', value)
else:
    newConfig.set('server', 'uri', userStoreUri)

with open(configfile, 'wb') as cfgfile:
    newConfig.write(cfgfile)

