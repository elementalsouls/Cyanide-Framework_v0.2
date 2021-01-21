#!/usr/bin/env python3
import subprocess
# import optparse
#
# parser = optparse.OptionParser()
# parser.add_option("-i", "--interface", dest="interface", help="Interfae to change it's Mac_Address.")
# parser.add_option("-m", "--mac", dest="mac_address", help="New Mac_Address.")
# (options, arguments) = parser.parse_args()
subprocess.call(["ip", "-br", "-c", "link", "show"])
interface = input("Please select your interface (eg.eth0/wlan0) : ")
mac_address = input("Please enter the mac_address.(eg.00:11:22:33:44:55) : ")
print("[+] Changing mac_address for :", interface + " to " + mac_address )
# This part is unsecure because any one can assign different commands within the input parameter
# subprocess.call("sudo ifconfig "+ interface +" down", shell=True)
# subprocess.call("sudo ifconfig "+ interface +" hw ether "+ mac_address, shell=True)
# subprocess.call("sudo ifconfig "+ interface +" up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])
print("[+] Your mac_address is successfully changed.[+]")

