from bluetooth import *
import time
import os

alreadyfound = []

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

def return_fw():
    bashCommand = ". ./cyanide-framework.sh && main"
    subprocess.call(['bash','-c', bashCommand])

def clearScr():
    os.system('clear')
def finddevs():
    foundDevs = discover_devices(lookup_names=True)
    for (addr, name) in foundDevs:
        if addr not in alreadyfound:
            print(color.WHITE+'[*] Found Bluetooth Device: '+color.RED + str(name) + color.WHITE+'\n    MAC address: '+color.RED + str(addr))
            alreadyfound.append(addr)
clearScr()
print(color.RED+"\t\t\tPlease Turn On Bluetooth Manually" )
time.sleep(10)


try:
    while True:
        finddevs()
        time.sleep(2)
except KeyboardInterrupt:
    return_fw()
