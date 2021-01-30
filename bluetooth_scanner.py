from bluetooth import *
import time

alreadyfound = []
def finddevs():
    foundDevs = discover_devices(lookup_names=True)
    for (addr, name) in foundDevs:
        if addr not in alreadyfound:
            print('[*] Found Bluetooth Device: ' + str(name) + '[+] MAC address: ' + str(addr))
            alreadyfound.append(addr)

while True:
    finddevs()
    time.sleep(5)

# for device in devList:
#     name = str(lookup_name(device))
#     print ("[+] Found Bluetooth Device " + str(name))
#     print ("[+] MAC address: "+str(device))