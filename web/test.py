#!/usr/bin/env python2

import os
import ConfigParser
import time
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
    print(color.RED+".,lol,..."+color.WHITE+"/_______/"+color.RED+".......,lol,.")
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

rsploit()

















# class Jtr:
#     def __init__(self):
#         if not self.installed():
#             self.install()
#             self.run()
#         else:
#             self.run()

#     def installed(self):
#         return (os.path.isfile("/usr/sbin/john")) or (os.path.isfile("/usr/bin/john")) or (os.path.isfile("/etc/john"))

#     def install(self):
#         os.system("sudo apt-get install john -y")

#     def run(self):
#         clearScr()
#         self.menu()

#     def menu(self):
#         clearScr()
#         logo()
#         print(color.RED + "\tEC-Council " + color.WHITE + "Methodology\n")
#         print(color.RED + " [ 1 ] Basic Hash Cracking (.txt) file")
#         print(color.WHITE + " [ 2 ] From Configuration File  ")
#         print(color.RED + " [ 99 ] Return to main-Menu \n")
#         response = int(input(color.RED + " select your option : "))
#         time.sleep(1.5)

#         try:
#             if response == 1:
#                 clearScr()
#                 logo()
#                 print(color.RED + "Formats are written as:\n")
#                 print(color.WHITE + " 1) md5 => raw-md5")
#                 print(color.WHITE + " 2) md4 => raw-md4")
#                 print(color.WHITE + " 3) sha1 ==>raw-sha1")
#                 print(color.WHITE + " 4) sha256 ==>raw-sha256")
#                 print(color.WHITE + " 1) md5 => raw-md5")
#                 format_known = raw_input("Do you know the hassh format[Y/n] : ")
#                 if (format_known == "Y") or (format_known == "y"):
#                     format = raw_input("Please Enter the Format: ")
#                     passwd_file_known = raw_input(color.WHITE+"Do you want to use a Custom Wordlist(Y/"+color.RED+("n:"))
#                     if (passwd_file_known == "Y") or (passwd_file_known == "y"):
#                         passwd_file = input(color.WHITE+"Enter the Custom Dictionary Location: ")
#                         file = input(color.WHITE+"Enter the hash file Location: ")
#                         print("Performing Hash Cracking")
#                         os.system("john --format=%s --wordlist=%s %s"%(format,passwd_file,file))
#                     elif passwd_file_known == "n":
#                         file = input(color.WHITE + "Enter the hash file Location: ")
#                         print("Performing Hash Cracking")
#                         os.system("john --format=%s %s" % (format,file))
#                     else:
#                         print("Wrong Option")
#                         Jtr.menu(self)
#                 elif format_known == "n":
#                     print(color.WHITE+"We can try it normally, but if this does not work, please use HashId in From other Section and Come Back")
#                     hid = raw_input(color.RED+"Do you want to use HashID(Y/n):")
#                     if hid == "Y":
#                         return_fw()
#                     elif hid == "n":
#                         passwd_file_known = input(color.WHITE + "Do you want to use a Custom Wordlist(Y/" + color.RED + ("n:"))
#                         if passwd_file_known == "Y":
#                             passwd_file = input(color.WHITE + "Enter the Custom Dictionary Location: ")
#                             file = input(color.WHITE + "Enter the hash file Location: ")
#                             print("Performing Hash Cracking")
#                             os.system("john --wordlist=%s %s" % (passwd_file, file))
#                         elif passwd_file_known == "n":
#                             file = input(color.WHITE + "Enter the hash file Location: ")
#                             print("Performing Hash Cracking")
#                             os.system("john %s" % file)
#                         else:
#                             print("Wrong Option")
#                             Jtr.menu(self)

#                     else:
#                         print("Wrong Option")
#                         Jtr.menu(self)

#             if response == 2:
#                 passwd_file = input(color.WHITE+"Do You have /etc/passwd (Y/"+color.RED+"n): ")
#                 shadow_file = input(color.WHITE+"Do You have /etc/shadow (Y/"+color.RED+"n): ")
#                 if shadow_file == "Y":
#                     if passwd_file == "Y":
#                         lcation = input(color.WHITE+"Location of custom /etc/passwd and /etc/shadow ")
#                         os.system("unshadow %s/etc/passwd %s/etc/shadow > crack.txt" %(lcation,lcation))
#                         os.system("john crack.txt")
#                     elif passwd_file == "n":
#                         lcation = input(color.WHITE + "Location of custom /etc/shadow ")
#                         os.system("john %s/etc/shadow" % lcation)
#                     else:
#                         Jtr.menu(self)
#                 if shadow_file == "n":
#                     if passwd_file == "Y":
#                         lcation = input(color.WHITE + "Location of custom /etc/passwd: ")
#                         os.system("john %s/etc/passwd" %lcation)
#                     else:
#                         Jtr.menu(self)

#         except KeyboardInterrupt:
#             # main()
#             pass

# Jtr()

# class Aircrack:

# def main():
#     clearScr()
#     logo()
#     print(color.RED + " [ 1 ] John the Ripper")
#     print(color.WHITE + " [ 2 ] Crawler")
#     print(color.RED + " [ 3 ] Dirb")
#     print(color.WHITE + " [ 4 ] Wapiti")
#     print(color.RED + " [ 5 ] WPScan")
#     print(color.WHITE + " [ 6 ] JoomScan")
#     print(color.RED + "[ 99 ]  Back To Framework")

#     response = int(input("\n Select your option : "))
#     try:
#         if response == 1:
#             clearScr()
#             Jtr()

    #     elif response == "2":
    #         clearScr()
    #         os.system("python3 crawler2.0.py")
    #
    #     elif response == "3":
    #         clearScr()
    #         dirb()
    #     elif response == "4":
    #         clearScr()
    #         wapiti()
    #
    #     elif response == "5":
    #         clearScr()
    #         wpscan()
    #
    #     elif response == "6":
    #         clearScr()
    #         joomscan()
    #
    #     elif response == "99":
    #         clearScr()
    #         return_fw()
    #
    #     else:
    #         main()
    #
#     except KeyboardInterrupt:
#         pass
#         # main()
# main()