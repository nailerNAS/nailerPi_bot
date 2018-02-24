# -*- coding: utf-8 -*-

import subprocess

try:
    from config import MAC, ETH0, WLAN0
except ImportError:
    MAC = ETH0 = WLAN0 = None


class NailerPI:
    def __init__(self, mac=MAC, eth0=ETH0, wlan0=WLAN0):
        assert not (mac is None)
        assert not (eth0 is None)
        assert not (wlan0 is None)

        self.mac = mac
        self.eth0 = eth0
        self.wlan0 = wlan0
    

    def online(self):
        msg = '_Reloeded!_\n\n\n{}'.format(self.ifconfig())
        return msg


    def run(self, cmd):
        try:
            proc = subprocess.Popen(cmd, executable='/bin/bash', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            return str(proc.stdout.read())
        except Exception as e:
            return str(e)
    

    def shutdown(self):
        return self.run('sudo poweroff')
    
    def reboot(self):
        return self.run('sudo reboot')
    
    def cpu_temp(self):
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'rt') as file:
                tmp = file.read()
            tmp = int(tmp) / 1000 # getting the right value
            tmp = round(tmp, 2)   # rouding it to two digits (optional)

            return str(tmp)
        except Exception as e:
            return str(e)
    

    def ethernet(self):
        return self.run('/sbin/ifconfig {}'.format(self.eth0))
    
    def wireless(self):
        return self.run('/sbin/ifconfig {}'.format(self.wlan0))
    
    def ifconfig(self):
        return self.run('/sbin/ifconfig')


    def wol(self):
        return self.run('/sbin/wakeonlan {}'.format(self.mac))