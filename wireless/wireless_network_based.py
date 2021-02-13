#!/usr/bin/env python2

import os
import ConfigParser
import time
import subprocess
import readline

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[37m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

def clearScr():
    os.system('clear')

def yesOrNo():
    return (input("Continue Y / N: ") in yes)

def return_fw():
    bashCommand = ". ./cyanide-framework.sh && main"
    output = subprocess.call(['bash','-c', bashCommand])

def logo():
    print(color.RED+"       ..,;:ccccccc:;...")
    print(color.WHITE+"    ..,clllc:;;;;;;:cllc,.")
    print(color.RED+"   .,cllc,..............';;'.")
    print(color.WHITE+"  .;lol;......"+color.WHITE+"_______"+color.RED+"....;lol;.")
    print(color.RED+" .,lol;......"+color.WHITE+"/ _____/"+color.RED+".....;lol;..  ")
    print(color.WHITE+" .coo......."+color.WHITE+"/ /"+color.RED+".............coo")
    print(color.RED+".'lol,....."+color.WHITE+"/ /"+color.RED+"............'lol,.")
    print(color.WHITE+".,lol,...."+color.WHITE+"/ /_____"+color.RED+"........,lol,.")
    print(color.RED+".,lol,...."+color.WHITE+"\______/"+color.RED+".......,lol,.")
    print(color.WHITE+" .:ooc'.................:ooc'")
    print(color.RED+"  .'cllc'.............cllc.")

installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
configFile = installDir + "/cyanide.cfg"
print(installDir)
config = ConfigParser.RawConfigParser()
config.read(configFile)

toolDir = installDir + config.get('cyanide', 'toolDir') # makes folder
logDir = installDir + config.get('cyanide', 'logDir') # make logs
yes = config.get('cyanide', 'yes').split()

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
# random.shuffle(color_random)
continuePrompt = "\nClick [Return] to continue"
alreadyInstalled = "Already Installed"

class fluxion:
    def __init__(self):
        self.installDir = toolDir + "fluxion"
        self.gitRepo = "https://github.com/FluxionNetwork/fluxion"

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile(installDir+ "tools/fluxion/fluxion.sh"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %(self.gitRepo, self.installDir))
        os.system("cd %s && chmod u+x fluxion.sh && ./fluxion -i" %self.installDir)


    def run(self):
        clearScr()
        self.menu()

    def menu(self):
        clearScr()
        logo()
        print(color.RED + "\tEC-Council " + color.WHITE + "Methodology\n")
        print(color.RED + " 1) Start Fluxion")
        print(color.WHITE + " 99) Return to Main-Menu \n")
        response = int(input(color.RED + " Select an Option : "))
        time.sleep(1.5)

        try:
            if response == 1:
                clearScr()
                logo()
                print(color.WHITE + "Starting Fluxion")
                time.sleep(2)
                clearScr()
                os.system("cd tools/fluxion &&./fluxion.sh")
            elif response == 99:
                main()
            else:
                fluxion.menu(self)
        except KeyboardInterrupt:
            fluxion.menu(self)

class airgeddon:
    def __init__(self):
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/airgeddon"))

    def install(self):
        os.system("sudo apt-get install airgeddon -y")

    def run(self):
        clearScr()
        self.menu()

    def menu(self):
        clearScr()
        logo()
        print(color.RED + "\tEC-Council " + color.WHITE + "Methodology\n")
        print(color.RED + " 1) Start Airgeddon")
        print(color.WHITE + " 99) Return to Main-Menu \n")
        response = int(input(color.RED + " Select an Option : "))
        time.sleep(1.5)

        try:
            if response == 1:
                clearScr()
                logo()
                print(color.WHITE+"Starting Airgeddon")
                time.sleep(2)
                clearScr()
                os.system("airgeddon")
            elif response == 99:
                main()
            else:
                airgeddon.menu(self)
        except KeyboardInterrupt:
            main()



def main():
    clearScr()
    logo()
    print(color.WHITE + " [ 1  ] Brute-Force Wi-Fi ")
    print(color.RED + " [ 2  ] Fluxion")
    print(color.WHITE + " [ 3  ] Bluetooth Scanner")
    print(color.RED + " [ 4  ] Airgeddon")
    print(color.WHITE + " [ 99 ] Back To Framework")

    response = raw_input(color.RED +"\n Select your option : ")
    try:
        if response == "1":
            clearScr()
            os.system("sudo python3 wireless/tweak.py")


        elif response == "2":
            clearScr()
            fluxion()

        elif response == "3":
            clearScr()
            os.system("python3 wireless/bt_scan.py")

        elif response == "4":
            clearScr()
            airgeddon()

        elif response == "99":
            clearScr()
            return_fw()

        else:
            main()

    except KeyboardInterrupt:
        main()
main()
