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
    subprocess.call(['bash','-c', bashCommand])

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

class Jtr:
    def __init__(self):
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/sbin/john")) or (os.path.isfile("/usr/bin/john")) or (os.path.isfile("/etc/john"))

    def install(self):
        os.system("sudo apt-get install john -y")

    def run(self):
        clearScr()
        self.menu()

    def menu(self):
        clearScr()
        logo()
        print(color.RED + "    EC-Council " + color.WHITE + "Methodology\n")
        print(color.RED + "  [ 1  ] Basic Hash Cracking (.txt) file")
        print(color.WHITE + "  [ 2  ] From Configuration File  ")
        print(color.RED + "\n  [ 99 ] Return to Main-Menu \n")
        response = int(input(color.WHITE + "  Select an Option : "))
        time.sleep(1.5)

        try:
            if response == 1:
                clearScr()
                logo()
                print(color.RED + "Formats are written as:\n")
                print(color.WHITE + " 1) md5 => raw-md5")
                print(color.WHITE + " 2) md4 => raw-md4")
                print(color.WHITE + " 3) sha1 ==>raw-sha1")
                print(color.WHITE + " 4) sha256 ==>raw-sha256")
                # print(color.WHITE + " 1) md5 => raw-md5")
                format_known = raw_input("Do you know the hash format[Y/n] : ")
                if (format_known == "Y") or (format_known == "y"):
                    format = raw_input("Please Enter the Format: ")
                    passwd_file_known = raw_input(color.WHITE+"Do you want to use a Custom Wordlist(Y/"+color.RED+("n:"))
                    if (passwd_file_known == "Y") or (passwd_file_known == "y"):
                        passwd_file = input(color.WHITE+"Enter the Custom Dictionary Location: ")
                        file = input(color.WHITE+"Enter the hash file Location: ")
                        print("Performing Hash Cracking")
                        os.system("john --format=%s --wordlist=%s %s"%(format,passwd_file,file))
                    elif passwd_file_known == "n":
                        file = input(color.WHITE + "Enter the hash file Location: ")
                        print("Performing Hash Cracking")
                        os.system("john --format=%s %s" % (format,file))
                    else:
                        print("Wrong Option")
                        Jtr.menu(self)
                elif format_known == "n":
                    print(color.WHITE+"We can try it normally, but if this does not work, please use HashId in From other Section and Come Back")
                    hid = raw_input(color.RED+"Do you want to use HashID(Y/n):")
                    if hid == "Y":
                        return_fw()
                    elif hid == "n":
                        passwd_file_known = input(color.WHITE + "Do you want to use a Custom Wordlist(Y/" + color.RED + ("n:"))
                        if passwd_file_known == "Y":
                            passwd_file = input(color.WHITE + "Enter the Custom Dictionary Location: ")
                            file = input(color.WHITE + "Enter the hash file Location: ")
                            print("Performing Hash Cracking")
                            os.system("john --wordlist=%s %s" % (passwd_file, file))
                        elif passwd_file_known == "n":
                            file = input(color.WHITE + "Enter the hash file Location: ")
                            print("Performing Hash Cracking")
                            os.system("john %s" % file)
                        else:
                            print("Wrong Option")
                            Jtr.menu(self)

                    else:
                        print("Wrong Option")
                        Jtr.menu(self)

            elif response == 2:
                passwd_file = input(color.WHITE+"Do You have /etc/passwd (Y/"+color.RED+"n): ")
                shadow_file = input(color.WHITE+"Do You have /etc/shadow (Y/"+color.RED+"n): ")
                if shadow_file == "Y":
                    if passwd_file == "Y":
                        lcation = input(color.WHITE+"Location of custom /etc/passwd and /etc/shadow ")
                        os.system("unshadow %s/etc/passwd %s/etc/shadow > crack.txt" %(lcation,lcation))
                        os.system("john crack.txt")
                    elif passwd_file == "n":
                        lcation = input(color.WHITE + "Location of custom /etc/shadow ")
                        os.system("john %s/etc/shadow" % lcation)
                    else:
                        Jtr.menu(self)
                if shadow_file == "n":
                    if passwd_file == "Y":
                        lcation = input(color.WHITE + "Location of custom /etc/passwd: ")
                        os.system("john %s/etc/passwd" %lcation)
                    else:
                        Jtr.menu(self)

            elif response == 99:
                main()

            else:
                print(color.RED+"Wrong Option")
                Jtr.menu(self)

        except KeyboardInterrupt:
            main()

class acrack:
    def __init__(self):
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/aircrack-ng")) or (os.path.isfile("/usr/sbin/aircrack-ng"))

    def install(self):
        os.system("sudo apt-get install aircrack-ng -y")

    def run(self):
        clearScr()
        self.menu()

    def menu(self):
        clearScr()
        logo()
        print(color.RED + "    EC-Council " + color.WHITE + "Methodology\n")
        print(color.RED + "  [ 1  ] Perform Basic Hash Cracking")
        print(color.WHITE + "\n  [ 99 ] Return to Main-Menu")
        response = int(raw_input(color.RED+"\n  Select the Option : "))
        if response == 1:
            file = raw_input(color.WHITE+"\n  Do you have a Custom Dictionary(Y/"+color.RED+"n): ")
            try:
                if (file == "Y") or (file == "y"):
                    lcation = raw_input(color.RED+"\n  Enter the Dictionary Path: ")
                    lcation2 = raw_input(color.WHITE+"\n  Enter the Path of Hashed File: ")
                    os.system("aircrack-ng -w %s %s" %(lcation, lcation2))
                elif (file == "N") or (file == "n"):
                    lcation2 = raw_input(color.WHITE + "\n  Enter the Path of Hashed File: ")
                    os.system("aircrack-ng -w /usr/share/wordlists/rockyou.txt %s" % lcation2)
                else:
                    print(color.RED+"\n  Wrong Option")
                    acrack.menu(self)
            except KeyboardInterrupt:
                acrack.menu(self)

        elif response == 99:
            main()
        else:
            print(color.RED+"Wrong Option")
            acrack.menu(self)

class ophcrack:
    def __init__(self):
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/ophcrack"))

    def install(self):
        os.system("sudo apt-get install ophcrack -y")

    def run(self):
        clearScr()
        self.menu()

    def menu(self):
        clearScr()
        logo()
        print(color.RED + "    EC-Council " + color.WHITE + "Methodology\n")
        print(color.RED + " [ 1  ] Basic Hash Cracking")
        print(color.WHITE + "\n [ 99 ] Return to Main-Menu")
        response = int(raw_input(color.RED+"\n Select an Option : "))
        try:
            if response == 1:
                time.sleep(2)
                os.system("ophcrack")

            elif response == 99:
                main()
            else:
                print(color.RED+"Wrong Option")
                ophcrack.menu(self)

        except KeyboardInterrupt:
            ophcrack.menu(self)

class cupp:
    def __init__(self):
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/etc/cupp.cfg"))

    def install(self):
        os.system("sudo apt-get install cupp -y")

    def run(self):
        clearScr()
        self.menu()

    def menu(self):
        clearScr()
        logo()
        print(color.RED + "    EC-Council " + color.WHITE + "Methodology\n")
        print(color.WHITE+" [ 1 ] CUPP Interactive Mode")
        print(color.RED+"\n [ 99 ] Back to Main-Menu")
        response = int(raw_input(color.WHITE+"\n Enter your Response: "))
        try:
            if response == 1:
                os.system("cupp -i")
            elif response == 99:
                main()
            else:
                print(color.RED+"  Wrong Option")
                cupp.menu(self)
        except KeyboardInterrupt:
            cupp.menu(self)

class hydra:
    def __init__(self):
        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/hydra"))

    def install(self):
        os.system("sudo apt-get install john -y")

    def run(self):
        clearScr()
        self.menu()

    def menu(self):
        clearScr()
        logo()
        print(color.RED + "    EC-Council " + color.WHITE + "Methodology\n")
        print(color.WHITE + "  Basic Service Brute Forcing")
        print(color.WHITE+"  Please select a Service")
        print(color.RED+" [ 1  ] SSH")
        print(color.WHITE+" [ 2  ] TELNET")
        print(color.RED + " [ 3  ] SMTP")
        print(color.WHITE + " [ 4  ] FTP")
        print(color.RED + " [ 5  ] SMB")
        print(color.WHITE + "\n [ 99 ] Back to Main Menu")
        response = int(raw_input(color.RED+"\n Select the Option : "))
        time.sleep(1.5)
        try:
            if response == 1:
                clearScr()
                logo()
                ip = raw_input(color.RED+"Enter the Target IP: ")
                rponse = raw_input(color.WHITE+"\n  Do you want add a Custom Dictionary(Y/"+color.RED+"n): ")
                if (rponse == "Y") or (rponse == "y"):
                    dict = raw_input(color.WHITE+"\n  Enter a Custom Dictionary Location: ")
                    os.system("hydra -L %s -P %s %s ssh" %(dict,dict,ip))
                elif (rponse == "N") or (rponse == "n"):
                    os.system("hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt %s ssh" % ip)
                else:
                    print(color.RED+ "\n  Wrong Option")
                    hydra.menu(self)

            if response == 2:
                clearScr()
                logo()
                ip = raw_input(color.RED + "\n  Enter the Target IP: ")
                rponse = raw_input(color.WHITE + "\n  Do you want add a Custom Dictionary(Y/" + color.RED + "n): ")
                if (rponse == "Y") or (rponse == "y"):
                    dict = raw_input(color.WHITE + "\n  Enter a Custom Dictionary Location: ")
                    os.system("hydra -L %s -P %s %s telnet" % (dict, dict, ip))
                elif (rponse == "N") or (rponse == "n"):
                    os.system("hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt %s telnet" % ip)
                else:
                    print(color.RED+"\n  Wrong Option")
                    hydra.menu(self)

            if response == 4:
                clearScr()
                logo()
                ip = raw_input(color.RED + "\n  Enter the Target IP: ")
                rponse = raw_input(color.WHITE + "\n  Do you want add a Custom Dictionary(Y/" + color.RED + "n): ")
                if (rponse == "Y") or (rponse == "y"):
                    dict = raw_input(color.WHITE + "\n  Enter a Custom Dictionary Location: ")
                    os.system("hydra -L %s -P %s %s FTP" % (dict, dict, ip))
                elif (rponse == "N") or (rponse == "n"):
                    os.system(
                        "hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt %s FTP" % ip)
                else:
                    print(color.RED+"\n  Wrong Option")
                    hydra.menu(self)

            if response == 3:
                clearScr()
                logo()
                ip = raw_input(color.RED + "\n  Enter the Target IP: ")
                uname=raw_input(color.WHITE +"\n  Enter the email address")
                rponse = raw_input(color.RED + "\n  Do you want add a Custom Dictionary(Y/" + color.RED + "n): ")
                if (rponse == "Y") or (rponse == "y"):
                    dict = raw_input(color.WHITE + "\n  Enter a Custom Dictionary Location: ")
                    os.system("hydra -l %s -P %s %s -e ns -V -s 465 smtp.gmail.com smtp" % (uname, dict, ip))
                elif (rponse == "N") or (rponse == "n"):
                    os.system("hydra -l %s -P /usr/share/wordlists/rockyou.txt %s -e ns -V -s 465 smtp.gmail.com smtp" %(uname, ip))
                else:
                    print("Wrong Option")
                    hydra.menu(self)
            if response == 5:
                clearScr()
                logo()
                ip = raw_input(color.RED + "\n  Enter the Target IP: ")
                rponse = raw_input(color.WHITE + "\n  Do you want add a Custom Dictionary(Y/" + color.RED + "n): ")
                if (rponse == "Y") or (rponse == "y"):
                    dict = raw_input(color.RED + "\n  Enter a Custom Dictionary Location: ")
                    os.system("hydra -L %s -P %s %s smb" % (dict, dict, ip))
                elif (rponse == "N") or (rponse == "n"):
                    os.system("hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt %s smb" % ip)
                else:
                    print(color.WHITE+ "\n  Wrong Option")
                    hydra.menu(self)

            if response == 99:
                hydra.menu(self)
        except KeyboardInterrupt:
            main()


def main():
    clearScr()
    logo()
    print(color.RED + "  [ 1  ] John the Ripper")
    print(color.WHITE + "  [ 2  ] Aircrack-ng")
    print(color.RED + "  [ 3  ] Ophcrack")
    print(color.WHITE + "  [ 4  ] CUPP")
    print(color.RED + "  [ 5  ] Hydra")
    print(color.WHITE + "\n  [ 99 ]  Back To Framework")

    response = raw_input(color.RED +"\n  Select your option : ")
    try:
        if response == "1":
            clearScr()
            Jtr()

        if response == "2":
            clearScr()
            acrack()

        elif response == "3":
            clearScr()
            ophcrack()

        elif response == "4":
            clearScr()
            cupp()

        elif response == "5":
            clearScr()
            hydra()

        elif response == "99":
            clearScr()
            return_fw()

        else:
            main()

    except KeyboardInterrupt:
        main()
main()
