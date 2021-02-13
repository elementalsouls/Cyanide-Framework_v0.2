#!/usr/bin/env python2

import os
import ConfigParser
import time
from time import gmtime, strftime, sleep
import subprocess

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
    return (raw_input("Continue Y / N: ") in yes)
def return_fw():
    bashCommand = ". ./cyanide-framework.sh && main"
    output = subprocess.call(['bash','-c', bashCommand])

installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
configFile = installDir + "/cyanide.cfg"
config = ConfigParser.RawConfigParser()
config.read(configFile)

toolDir = installDir + config.get('cyanide', 'toolDir')
logDir = installDir + config.get('cyanide', 'logDir')
yes = config.get('cyanide', 'yes').split()

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
# random.shuffle(color_random)
continuePrompt = "\nClick [Return] to continue"
alreadyInstalled = "Already Installed"
output = os.path.isfile(installDir+ "tools/hiddeneye/HiddenEye.py")
print(output)
class hiddeneye():
    def __init__(self):
        self.installDir = toolDir + "hiddeneye"
        self.gitRepo = "https://github.com/DarkSecDevelopers/HiddenEye-Legacy.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = raw_input(continuePrompt)
        return_fw()

    def installed(self):
        return (os.path.isfile(installDir+ "tools/hiddeneye/HiddenEye.py"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && python3 HiddenEye.py install" % self.installDir)

    def run(self):
        os.system("cd %s && python3 HiddenEye.py install" % self.installDir)

# hiddeneye()



class blackeye():
    def __init__(self):
        self.installDir = toolDir + "blackeye"
        self.gitRepo = "https://github.com/x3rz/blackeye.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = raw_input(continuePrompt)

    def installed(self):
        return (os.path.isfile(installDir+ "tools/blackeye/blackeye.sh"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && bash blackeye.sh" % self.installDir)

    def run(self):
        os.system("cd %s && bash blackeye.sh" % self.installDir)

# blackeye()

class socialphish():
    def __init__(self):
        self.installDir = toolDir + "socialphish"
        self.gitRepo = "https://github.com/xHak9x/SocialPhish.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = raw_input(continuePrompt)
        return_fw()

    def installed(self):
        return (os.path.isfile(installDir+ "tools/SocialPhish/socialphish.sh"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && chmod +x socialphish.sh" % self.installDir)

    def run(self):
        os.system("cd %s && chmod +x socialphish.sh && bash socialphish.sh" % self.installDir)

# socialphish()


class AdvPhishing():
    def __init__(self):
        self.installDir = toolDir + "AdvPhishing"
        self.gitRepo = "https://github.com/Ignitetch/AdvPhishing.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = raw_input(continuePrompt)
        return_fw()

    def installed(self):
        return (os.path.isfile(installDir+ "tools/AdvPhishing/AdvPhishing.sh"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && chmod 777 * && bash Linux-Setup.sh" % self.installDir)

    def run(self):
        os.system("cd %s && chmod 777 * && bash AdvPhishing.sh" % self.installDir)

# AdvPhishing()


class zphisher():
    def __init__(self):
        self.installDir = toolDir + "zphisher"
        self.gitRepo = "https://github.com/htr-tech/zphisher.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = raw_input(continuePrompt)
        return_fw()

    def installed(self):
        return (os.path.isfile(installDir+ "tools/zphisher/zphisher.sh"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && chmod +x zphisher.sh" % self.installDir)

    def run(self):
        os.system("cd %s && chmod +x zphisher.sh && bash zphisher.sh" % self.installDir)

# zphisher()

class nexphisher():
    def __init__(self):
        self.installDir = toolDir + "nexphisher"
        self.gitRepo = "https://github.com/htr-tech/nexphisher.git"
        # self.return_main()
        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = raw_input(continuePrompt)
        return_fw()        

    def installed(self):
        return (os.path.isfile(installDir+ "tools/nexphisher/nexphisher.sh"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && chmod 777 * && bash setup" % self.installDir)

    def run(self):
        os.system("cd %s && chmod 777 * && bash nexphisher" % self.installDir)

# nexphisher()
class main():

    clearScr()
    
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
    print(color.RED+"   [ 1  ] HiddenEye")
    print(color.WHITE+"   [ 2  ] Blackeye")
    print(color.RED+"   [ 3  ] SocialPhish")
    print(color.WHITE+"   [ 4  ] AdvPhishing")
    print(color.RED+"   [ 5  ] zphisher")
    print(color.WHITE+"   [ 6  ] nexphisher")
    print(color.RED+"\n   [ 99  ] Return to main-menu")

    response = raw_input("\n   select your option : ")
    try:
        if response == "1":
            clearScr()
            hiddeneye()
            main()

        elif response == "2":
            clearScr()
            blackeye()
            main()

        elif response == "3":
            clearScr()
            socialphish()
            main()

        elif response == "4":
            clearScr()
            AdvPhishing()
            main()
        elif response == "5":
            clearScr()
            zphisher()
            main()

        elif response == "6":
            clearScr()
            nexphisher()
            # main()
        elif response == "99":
            print("\n\t Returning to main-menu")
            return_fw()
            # bashCommand = "clear;. ./cyanide-framework.sh;main"
            # output = subprocess.call(['bash','-c', bashCommand])


        else:
            self.menu(target)
    except KeyboardInterrupt:
        self.menu(target)


main()
