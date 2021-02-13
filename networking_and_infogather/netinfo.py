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

class nmap:
    def __init__(self):
        self.installDir = toolDir + "nmap"
        self.gitRepo = "https://github.com/nmap/nmap.git"

        self.targetPrompt = color.RED+"\nLock Your Target "+color.WHITE+"IP/Subnet/Range/Host: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))


    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && ./configure && make && make install" %
                  self.installDir)

    def run(self):
        clearScr()
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(color.RED+"   Target Locked : "+color.WHITE +str(target)+"\n")
        print(color.RED+"\tEC-Council "+color.WHITE+"Methodology\n")
        print(color.RED+" [ 1  ] SYN Network [-sS]")
        print(color.WHITE+" [ 2  ] ACK Network [-A]")
        print(color.RED+" [ 3  ] Aggressive Scan [-A/-T4]")
        print(color.WHITE+" [ 4  ] X-mas Scan [-SX]")
        print(color.RED+" [ 5  ] Ping Network [-sn]")
        print(color.WHITE+" [ 6  ] Normal Scan ")
        print(color.RED+" [ 7  ] Detect OS [-O]")
        print(color.WHITE+" [ 8  ] Selective Port Scan [-p]")
        print(color.RED+" [ 9  ] Firewall Evasion [--script]")
        print(color.WHITE+" [ 10  ] Host Discovery [-Pn]")
        print(color.RED+" [ 11  ] Connect Scan [-sT]\n")
        print(color.RED+" \tOptional "+color.WHITE+"Scans\n")
        print(color.RED+" [ 12  ] Server Ports Scan[-sT/-sS/80/443]")
        print(color.WHITE+" [ 13  ] Hidden Mode [Decoy]")
        print(color.RED+" [ 14  ] Scan all vulnerabilities using Script[--script]\n")
        print(color.WHITE+" [ 99 ] Return to main-Menu \n")
        response = raw_input(color.RED+" select your option : ")
        clearScr()
        # logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            print(target)
            if response == "1":
                os.system("sudo nmap -sS %s" % target )
                # os.system("sudo nmap -sn %s" % target )
                # os.system("nmap -sV -oN %s" % target)
                response = raw_input(continuePrompt)
                nmap()
            elif response == "2":
                os.system("sudo nmap -A %s" % target )
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "3":
                os.system("sudo nmap -A -T4 %s" % target )
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "4":
                os.system("sudo nmap -SX %s" % target )
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "5":
                os.system("sudo nmap -sn %s" % target )
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "6":
                os.system("sudo nmap %s" % target )
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "7":
                os.system("sudo nmap -O %s" % target )
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "8":
                response = raw_input("\nPlease Enter the Port : ")
                os.system("sudo nmap -p %s %s" % (response, target))
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "9":
                os.system("sudo nmap --script firewall-bypass %s" % target )
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "10":
                os.system("sudo nmap -Pn %s" % target )
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "11":
                os.system("sudo nmap -sT %s" % target )
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "12":
                print(color.WHITE+" [ 1  ] Normal Scan [-sT]")
                print(color.RED+" [ 2  ] Stealthy scan(hidden) [-sS]")
                response = raw_input("\nselect your option : ")
                try:
                    if response == "1":
                        os.system("sudo nmap -sT -p 80,443 %s" % target )
                        response = raw_input(continuePrompt)
                        clearScr()
                        nmap()
                    elif response == "2":
                        os.system("sudo nmap -sS -p 80,443 %s" % target )
                        response = raw_input(continuePrompt)
                        clearScr()
                        nmap()
                    else:
                        print("\n\tWrong input")
                        sleep(1)
                        self.menu(target)
                except KeyboardInterrupt:
                    response = raw_input(continuePrompt)
                    menu()
            elif response == "13":
                response = raw_input(color.WHITE+"\nEnter the decoy IPaddress Here : ")
                os.system("sudo nmap -sS -D %s %s" %(response, target))
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "14":
                print(color.WARNING+"Have patience! This may take some time\n")
                os.system("sudo nmap --script vuln %s" % target)
                response = raw_input(continuePrompt)
                clearScr()
                nmap()
            elif response == "99":
                sleep(0.5)
                clearScr()
                return_fw()
            else:
                self.menu(target)
        except KeyboardInterrupt:
            response = raw_input(continuePrompt)
            menu(self)


class wpscan:
    def __init__(self):
        self.installDir = toolDir + "wpscan"
        self.gitRepo = "https://github.com/wpscanteam/wpscan.git"

        if not self.installed():
            self.install()
        clearScr()
        print(color.WHITE+"\n\t [ WPSCAN ]")
        target = raw_input(color.RED+"\n Enter a Target: ")
        self.menu(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))

    def menu(self, target):
        clearScr()
        logo()
        print(color.RED+"\n\tTarget Locked : "+color.WHITE+ str(target)+"\n")
        print(color.RED+" [ 1  ] Username Enumeration [--enumerate u]")
        print(color.WHITE+" [ 2  ] Plugin Enumeration [--enumerate p]")
        print(color.RED+" [ 3  ] All Enumeration Tools [--enumerate]\n")
        print(color.WHITE+" [ 99  ] Return to information gathering menu \n")
        response = raw_input(" Select Your Options : ")
        clearScr()
        logPath = "../../logs/wpscan-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        wpscanOptions = "--no-banner --random-agent --url %s" % target
        locate_wpscan = os.popen("locate wpscan.rb").read().rstrip("\n")
        try:
            if response == "1":
                os.system(
                    "ruby " + locate_wpscan + " --enumerate u --log %s %s" % (wpscanOptions, logPath))
                response = raw_input(continuePrompt)
                return_fw()
            elif response == "2":
                os.system(
                    "ruby " + locate_wpscan + " --enumerate u --log %s %s" % (wpscanOptions, logPath))
                response = raw_input(continuePrompt)
                return_fw()
            elif response == "3":
                os.system(
                    "ruby " + locate_wpscan + " --enumerate u --log %s %s" % (wpscanOptions, logPath))
                response = raw_input(continuePrompt)
                return_fw()
            elif response == "99":
                sleep(0.5)
                clearScr()
                return_fw()
            else:
                self.menu(target)
        except KeyboardInterrupt:
            menu()


class setoolkit:
    def __init__(self):
        self.installDir = toolDir + "setoolkit"
        self.gitRepo = "https://github.com/trustedsec/social-engineer-toolkit.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = raw_input(continuePrompt)
        return_fw()

    def installed(self):
        return (os.path.isfile("/usr/bin/setoolkit"))

    def install(self):
        os.system("apt-get --force-yes -y install git apache2 python-requests libapache2-mod-php \
            python-pymssql build-essential python-pexpect python-pefile python-crypto python-openssl")
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && python setup.py install" % self.installDir)

    def run(self):
        os.system("setoolkit")

class crips:
    def __init__(self):
        self.installDir = toolDir + "Crips"
        self.gitRepo = "https://github.com/Manisso/Crips"
        # self.targetPrompt = color.RED + "\nLock Your Target " + color.WHITE + "IP/Subnet/Range/Host: "
        if self.installed():
            self.run()
        else:
            self.install()
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/share/doc/Crips/crips.py"))

    def install(self):
        os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        os.system("cd %s && chmod u+x install.sh && sleep 2.5 && ./install.sh && cd .." % self.installDir)

    def run(self):
        clearScr()
        self.menu()

    def menu(self):
        print(color.WHITE + "EC-Council" + color.RED + "Methodology\n")
        print(color.WHITE + "Starting Crips")
        os.system("cd /usr/share/doc/Crips && python crips.py")

class rsploit:
    def __init__(self):
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/routersploit"))

    def install(self):
        os.system("sudo apt-get install routersploit -y")
        os.system("routersploit")
    def run(self):
        clearScr()
        os.system("routersploit")
        


def main():
    clearScr()
    logo()
    print(color.RED+"  [ 1  ] nmap")
    print(color.WHITE+"  [ 2  ] setoolkit")
    print(color.RED+"  [ 3  ] WPScan")
    print(color.WHITE+"  [ 4  ] Mac_Changer")
    print(color.RED+"  [ 5  ] Crips")
    print(color.WHITE+"  [ 6  ] Router-Sploit")
    print(color.WHITE+"\n  [ 99 ] Return to main-Menu \n")

    response = raw_input(color.RED+"  select your option : ")
    try:
        if response == "1":
            clearScr()
            nmap()
            main()

        elif response == "2":
            clearScr()
            setoolkit()
            main()
        elif response == "3":
            clearScr()
            wpscan()
            main()
        elif response == "4":
            clearScr()
            print(color.RED+"\t [ MAC "+color.WHITE+"Changer ]\n" )
            os.system("python3 mac_changer.py")
            main()
        elif response == "5":
            clearScr()
            crips()
            main()
        elif response == "6":
            clearScr()
            rsploit()
            main()
        elif response == "99":
            print("\n\t Returning to main-menu ")
            sleep(0.5)
            clearScr()
            return_fw()


        else:
            print(color.RED+"\tWorng Option! Try Again")
            sleep(1)
            main()
    except KeyboardInterrupt:
        return_fw()

main()

