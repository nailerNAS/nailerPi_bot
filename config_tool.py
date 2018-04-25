# -*- coding: utf-8 -*-

try:
    from config import TOKEN
except ImportError:
    TOKEN = None
try:
    from config import ADMIN
except ImportError:
    ADMIN = None
try:
    from config import MAC
except ImportError:
    MAC = None
try:
    from config import ETH0
except ImportError:
    ETH0 = None
try:
    from config import WLAN0
except ImportError:
    WLAN0 = None

def try_int(param: str) -> bool:
    try:
        int(param)
        return True
    
    except ValueError:
        return False

config = {
    'token': TOKEN,
    'admin': ADMIN,
    'mac': MAC,
    'eth0': ETH0,
    'wlan0': WLAN0
}

print('Welcome to nailerPi configuration tool!\n\n')

while True:
    print('\nYour current settings below:\n')

    for key in config.keys():
        print('%s: %s' % (key, config[key]))

    print('\n')

    param = input('Which option would you like to change: ')

    if param in config.keys():
        new_value = None
        new_value = input('New value: ')

        if new_value:
            config[param] = new_value if not try_int(new_value) else int(new_value)
            print('\nReturning. You can enter zero, quit or exit commands to save changes and exit\n')

        else:
            print('No value given, returning to the settings list')

    elif param in ['0', 'exit', 'quit']:
        config_string = ''
        
        for key in config.keys():
            config_string += '%s = ' % (key)
            config_string += str(config[key]) if try_int(config[key]) else "'%s'" % (config[key])
            config_string += '\n'
        
        with open('config.py', 'wt') as config_file:
            config_file.write(config_string)
        
        print('Config is written successfully. Exiting. . .')
        break

    else:
        print('\nUnknown option\n')