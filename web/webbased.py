#!/usr/bin/env python2

import os
import ConfigParser
import time
from time import gmtime, strftime, sleep
import lib
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
def logo():
    print(color.RED+"       ..,;:ccccccc:;...")
    print(color.WHITE+"    ..,clllc:;;;;;;:cllc,.")
    print(color.RED+"   .,cllc,..............';;'.")
    print(color.WHITE+"  .;lol;......"+color.WHITE+"_______"+color.RED+"....;lol;.")
    print(color.RED+" .,lol;......"+color.WHITE+"/ _____/"+color.RED+".....;lol;..  ")
    print(color.WHITE+" .coo......."+color.WHITE+"/ /"+color.RED+".............coo")
    print(color.RED+".'lol,....."+color.WHITE+"/ /"+color.RED+"............'lol,.")
    print(color.WHITE+".,lol,...."+color.WHITE+"/ /_____"+color.RED+"........,lol,.")
    print(color.RED+".,lol,..."+color.WHITE+"/_______/"+color.RED+".......,lol,.")
    print(color.WHITE+" .:ooc'.................:ooc'")
    print(color.RED+"  .'cllc'.............cllc.")

def clearScr():
    os.system('clear')

def yesOrNo():
    return (raw_input("Continue Y / N: ") in yes)

def return_fw():
    bashCommand = ". ./cyanide-framework.sh && main"
    output = subprocess.call(['bash','-c', bashCommand])

installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
configFile = installDir + "/cyanide.cfg"
print(installDir)
config = ConfigParser.RawConfigParser()
config.read(configFile)

toolDir = installDir + config.get('cyanide', 'toolDir')
logDir = installDir + config.get('cyanide', 'logDir')
yes = config.get('cyanide', 'yes').split()

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
# random.shuffle(color_random)
continuePrompt = "\nClick [Return] to continue"
alreadyInstalled = "Already Installed"

class nikto:
    def __init__(self):
        self.installDir = toolDir + "nikto"
        self.gitRepo = "https://github.com/sullo/nikto"

        self.targetPrompt = color.RED+"\nLock Your Target "+color.WHITE+"IP/Subnet/Range/Host: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nikto") or os.path.isfile("/usr/local/bin/nikto"))


    def install(self):
        # os.system("git clone --depth=1 %s %s" %
        #           (self.gitRepo, self.installDir))
        # os.system("cd %s && ./configure && make && make install" %
        #           self.installDir)
        os.system("sudo apt-get install nikto -y")
    def run(self):
        clearScr()
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        logo()
        print(color.RED + "  Target Locked : " + color.WHITE + str(target) + "\n")
        print(color.RED + "   OWASP " + color.WHITE + "Top 10 " + color.RED +"Methodology\n")
        print(color.RED + " [ 1  ] Basic Scan")
        print(color.WHITE + " [ 2  ] Specific Port Scan")
        print(color.RED + " [ 3  ] Output Storing\n")
        print(color.WHITE + " [ 99 ] Return to main-Menu \n")
        response = int(raw_input(color.RED+" select your option : "))
        clearScr()
        # logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            print(color.RED + target)

            if response == 1:
                clearScr()
                logo()
                print(color.RED +"[*] Scanning For Basic Vulnerablities...\n")
                time.sleep(1)
                os.system("sudo nikto -h %s" % target)
            elif response == 2:
                clearScr()
                logo()    
                time.sleep(1)
                print(color.RED + "Use ',' to put multiple ports. ")
                ports = raw_input(color.RED + "Enter Port Numbers: ")
                print(color.WHITE + "[*] Scanning For Specific Ports...\n")
                os.system("sudo nikto -h %s -p %s" % (target,ports))
            elif response == 3:
                clearScr()
                logo()
                print(color.RED + "  Doing Output Storing Scan...\n")
                print(color.WHITE + "  Please Select Output Forms:\n")
                print(color.RED +"  [1] CSV\n" + color.WHITE + "  [2] txt\n" + color.RED + "  [3] xml\n")
                response = int(raw_input("Choose Your Option: "))
                try:
                    if response == 1:
                        os.system("sudo nikto -h %s -o nikto_result -F csv" % target)
                    elif response == 2:
                        os.system("sudo nikto -h %s -o nikto_result -F txt" % target)
                    elif response == 3:
                        os.system("sudo nikto -h %s -o nikto_result -F xml" % target)
                    else:
                        print(color.RED + "Wrong Option")
                except KeyboardInterrupt:
                    response = raw_input(continuePrompt)
                    return_fw()
            elif response == "99":
                sleep(0.5)
                clearScr()
                return_fw()
            else:
                self.menu(target)
        except KeyboardInterrupt:
            response = raw_input(continuePrompt)
            return_fw()

class dirb:
    def __init__(self):
        self.installDir = toolDir + "dirb"
        self.gitRepo = "https://github.com/sullo/nikto"

        self.targetPrompt = color.RED+"\nLock Your Target "+color.WHITE+"IP/Subnet/Range/Host: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/dirb") or os.path.isfile("/usr/local/bin/dirb"))


    def install(self):
        # os.system("git clone --depth=1 %s %s" %
        #           (self.gitRepo, self.installDir))
        # os.system("cd %s && ./configure && make && make install" %
        #           self.installDir)
        os.system("sudo apt-get install dirb -y")
    def run(self):
        clearScr()
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        logo()
        print(color.RED + "  Target Locked : " + color.WHITE + str(target) + "\n")
        print(color.RED + "  OWASP " + color.WHITE + "Top 10 " + color.RED + "Methodology\n")
        print(color.RED + " [ 1  ] Basic Scan")
        print(color.WHITE + " [ 2  ] Silent Mode")
        print(color.RED + " [ 3  ] Output Storing\n\n")
        print(color.WHITE + " [ 99 ] Return to main-Menu \n")
        response = int(raw_input(color.RED + " select your option : "))
        clearScr()
        # logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            print(color.RED + target)
            if response == 1:
                clearScr()
                logo()
                print(color.RED +"[*] Doing Basic Scan\n")
                sleep(1)
                os.system("sudo dirb %s" % target)
            elif response == 2:
                clearScr()
                logo()
                print(color.WHITE + "Doing Silent Scan\n")
                sleep(1)
                os.system("sudo dirb %s -S" % target)
            elif response == 3:
                clearScr()
                logo()
                print(color.RED + "  Doing Output Storing Scan\n")
                print(color.WHITE + "  Please Select the Output Forms:\n")
                print(color.RED +"  [1] CSV\n" + color.WHITE + "  [2] txt\n")
                response = int(raw_input("  Choose Your Option: "))
                try:
                    if response == 1:
                        os.system("sudo dirb %s -o dirb_result.csv" % target)
                    elif response == 2:
                        os.system("sudo dirb %s -o dirb_result.txt" % target)
                    else:
                        print(color.RED + "Wrong Option")
                except KeyboardInterrupt:
                    response = raw_input(continuePrompt)
                    return_fw()
            elif response == "99":
                sleep(0.5)
                clearScr()
                return_fw()
            else:
                self.menu(target)
        except KeyboardInterrupt:
            response = raw_input(continuePrompt)
            return_fw()

class wapiti:
    def __init__(self):
        self.installDir = toolDir + "wapiti"
        self.gitRepo = "https://sourceforge.net/projects/wapiti/files/latest/download"

        self.targetPrompt = color.RED+"\nLock Your Target "+color.WHITE+"IP/Subnet/Range/Host[With headers]: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return os.path.isfile("/usr/bin/wapiti")


    def install(self):
        os.system("cd %s && wget %s && sleep 3" %(self.installDir, self.gitRepo))
        os.system("unzip download && sleep 5 && cd wapiti3-3.0.3/")

    def run(self):
        clearScr()
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        logo()
        print(color.RED + "   Target Locked : " + color.WHITE + str(target) + "\n")
        print(color.RED + "   OWASP " + color.WHITE + "Top 10 " + color.RED +"Methodology\n")
        print(color.RED + " [ 1 ] Basic Scan")
        print(color.WHITE + " [ 2 ] Skip Crawl")
        print(color.RED + " [ 3 ] Output Storing\n\n")
        print(color.WHITE + " [ 99 ] Return to main-Menu \n")
        response = raw_input(color.RED+" select your option : ")
        clearScr()
        try:
            print(target)
            if response == "1":
                os.system("sudo wapiti -u %s" % target)
                # os.system("sudo nmap -sn %s" % target )
                # os.system("nmap -sV -oN %s" % target)
                response = raw_input(continuePrompt)
                wapiti()
            elif response == "2":
                os.system("sudo wapiti -u %s --skip-crawl " % target)
                response = raw_input(continuePrompt)
                clearScr()
                wapiti()
            elif response == "3":
                clearScr()
                logo()
                print(color.WHITE+" \n   Doing Output Storing Scan\n")
                print(color.RED+" [ 1  ] html")
                print(color.WHITE+" [ 2  ] txt")
                print(color.RED+" [ 3  ] xml")
                print(color.WHITE + "\n [ 99 ] Back to menu \n")
                response = raw_input("\nselect your option : ")
                try:
                    if response == "1":
                        os.system("sudo wapiti -u %s -o wapiti_result -f html" % target)
                        response = raw_input(continuePrompt)
                        clearScr()
                        wapiti()
                    elif response == "2":
                        os.system("sudo wapiti -u %s -o wapiti_result -f txt" % target)
                        response = raw_input(continuePrompt)
                        clearScr()
                        wapiti()
                    elif response == "3":
                        os.system("sudo wapiti -u %s -o wapiti_result -f xml" % target)
                        response = raw_input(continuePrompt)
                        clearScr()
                        wapiti()
                    else:
                        print("\n\tWrong input")
                        sleep(1)
                        self.menu(target)
                except KeyboardInterrupt:
                    response = raw_input(continuePrompt)
                    # return_fw()
                    menu()

        except KeyboardInterrupt:
            pass


class wpscan:
    def __init__(self):
        self.targetPrompt = color.RED + "\nLock Your Target " + color.WHITE + "IP/Subnet/Range/Host: "
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/wpscan"))

    def install(self):
        os.system("sudo ap-get install wpscan -y")

    def run(self):
        clearScr()
        target2 = raw_input(self.targetPrompt)
        target = "https://" + target2
        self.menu(target)

    def menu(self, target):
        clearScr()
        logo()
        print(color.RED + "   Target Locked : " + color.WHITE + str(target) + "\n")
        print(color.RED + "\tOWASP " + color.WHITE + "Top 10 " + color.RED + "Methodology\n")
        print(color.RED + " [ 1 ] Basic Scan with Enumeration")
        print(color.WHITE + " [ 2 ] Enumerate Username")
        print(color.RED + " [ 3 ] Enumerate Passwords")
        print(color.RED + " [ 4 ] Store Output")
        print(color.WHITE + " [ 99 ] Return to main-Menu \n")
        response = int(raw_input(color.RED + " select your option : "))
        sleep(2.5)

        try:
            print(color.RED + target)
            if response == 1:
                clearScr()
                logo()
                print(color.RED + "[*] Doing Basic Scan\n")
                sleep(1)
                os.system("sudo wpscan --url %s --enumerate" % target)
            elif response == 2:
                clearScr()
                logo()
                print(color.WHITE + "Enumerating Usernames\n")
                sleep(1)
                os.system("sudo wpscan --url %s --enumerate u " % target)
            elif response == 3:
                clearScr()
                logo()
                uname = raw_input(color.RED+ "Please Enter the above shown Username: ")
                sleep(1)
                os.system("sudo wpscan --url %s --wordlist = /usr/share/wordlist/rockyou.txt --enumerate --username = %s " %(target, uname))
            elif response == 4:
                clearScr()
                logo()
                print(color.RED + "[*] Doing Basic Scan with Enumeration and Saving Output\n")
                sleep(1)
                os.system("sudo wpscan --url %s --enumerate -o wpscan -f json" % target)
            elif response == 99:
                main()
            else:
                print("Wrong Option")
                self.menu(target)

        except KeyboardInterrupt:
            main()

class joomscan:
    def __init__(self):
        self.targetPrompt = color.RED + "\nLock Your Target " + color.WHITE + "IP/Subnet/Range/Host: "
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
            return (os.path.isfile("/usr/bin/joomscan"))

    def install(self):
            os.system("sudo ap-get install joomscan -y")

    def run(self):
        clearScr()
        target2 = raw_input(self.targetPrompt)
        target = "https://" + target2
        self.menu(target)

    def menu(self,target):
        clearScr()
        logo()
        print(color.RED + "   Target Locked : " + color.WHITE + str(target) + "\n")
        print(color.RED + "\tOWASP " + color.WHITE + "Top 10 " + color.RED + "Methodology\n")
        print(color.RED + " [ 1 ] Basic Scan")
        print(color.WHITE + " [ 2 ] Enumerate Components")
        print(color.RED + " [ 99 ] Return to main-Menu \n")
        print(color.WHITE + "Output is Automatically Stored in: \n /usr/share/reports/"+color.RED +"%s" % target)
        response = int(raw_input(color.RED + " select your option : "))
        sleep(2.5)

        try:
            print(color.RED + target)
            if response == 1:
                clearScr()
                logo()
                print(color.RED + "[*] Doing Basic Scan\n")
                time.sleep(1)
                os.system("sudo joomscan -u %s" % target)
            elif response == 2:
                clearScr()
                logo()
                print(color.WHITE + "Enumerating Components\n")
                time.sleep(1)
                os.system("sudo joomscan -u %s -ec " % target)
            elif response == 99:
                main()
            else:
                print("Wrong Option")
                self.menu(target)

        except KeyboardInterrupt:
            main()


def main():
    clearScr()
    logo()
    print(color.RED + "   OWASP " + color.WHITE + "Top 10 " + color.RED +"Methodology\n")
    print(color.RED + "  [ 1  ] Nikto")
    print(color.WHITE + "  [ 2  ] Crawler")
    print(color.RED + "  [ 3  ] Dirb")
    print(color.WHITE + "  [ 4  ] Wapiti")
    print(color.RED + "  [ 5  ] WPScan")
    print(color.WHITE + "  [ 6  ] JoomScan\n")
    print(color.RED + "  [ 99 ]  Back To Framework")

    response = raw_input("\n  Select your option : ")
    try:
        if response == "1":
            clearScr()
            nikto()

        elif response == "2":
            clearScr()
            os.system("sudo python3 web/crawler2.0.py")

        elif response == "3":
            clearScr()
            print("This is menu")
            dirb()
        elif response == "4":
            clearScr()
            wapiti()

        elif response == "5":
            clearScr()
            wpscan()

        elif response == "6":
            clearScr()
            joomscan()

        elif response == "99":
            clearScr()
            return_fw()

        else:
            main()

    except KeyboardInterrupt:
        # main()
        pass

main()
