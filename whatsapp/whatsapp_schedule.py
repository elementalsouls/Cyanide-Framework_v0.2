import colorama
import os
import subprocess
import pywhatkit
from time import sleep
from colorama import Fore, Back, Style
import tqdm
from tqdm.auto import tqdm
colorama.init(autoreset=True)

def return_fw():
    bashCommand = ". ./cyanide-framework.sh && main"
    output = subprocess.call(['bash','-c', bashCommand])
    
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('clear')

def user_input_1():
  global number
  print(Fore.RED+"       ..,;:ccccccc:;...")
  print(Fore.WHITE+"    ..,clllc:;;;;;;:cllc,.")
  print(Fore.RED+"   .,cllc,..............';;'.")
  print(Fore.WHITE+"  .;lol;......"+Fore.WHITE+"_______"+Fore.RED+"....;lol;.")
  print(Fore.RED+" .,lol;......"+Fore.WHITE+"/ _____/"+Fore.RED+".....;lol;..  ")
  print(Fore.WHITE+" .coo......."+Fore.WHITE+"/ /"+Fore.RED+".............coo")
  print(Fore.RED+".'lol,....."+Fore.WHITE+"/ /"+Fore.RED+"............'lol,.")
  print(Fore.WHITE+".,lol,...."+Fore.WHITE+"/ /_____"+Fore.RED+"........,lol,.")
  print(Fore.RED+".,lol,...."+Fore.WHITE+"\______/"+Fore.RED+".......,lol,.")
  print(Fore.WHITE+" .:ooc'.................:ooc'")
  print(Fore.RED+"  .'cllc'.............cllc.")
  print(Fore.WHITE+ Back.RED + "[ℂ] make sure you have logged \ninto web.whatsapp.com on your \ndefault web browser. [ℂ]")
  print("\n")
  number = input(Fore.WHITE+ "[ℂ] Enter mobile number with country code :")
  if number[0] != "+" :
    print(Fore.RED+ "\n\t【X】Please enter correct country code (eg.+919876543210)【X】")
    sleep(2)
    screen_clear()
    user_input_1()
  elif len(number) != 13:
    print(Fore.RED+ "\n\t【X】Please enter the correct number with country code (eg.+919876543210)【X】")
    sleep(2)
    screen_clear()
    user_input_1()
  else:
    pass
    
def execute():
  screen_clear()
  user_input_1()
  user_message = input(Fore.WHITE+ "\n[ℂ] Enter your message here :")
  time_in_hour = int(input(Fore.RED+ "\n[ℂ] Enter the hour (max:24) :"))
  time_in_minute = int(input(Fore.WHITE+ "\n[ℂ] Enter the hour (max:60) :"))
  
  # This will open web.whatsapp.com at 14:59:40 and message will be sent at exactly 15:00:00
  # pywhatkit.sendwhatmsg("+919344562333", "Hello", 16,24)
  sleep(1)
  pywhatkit.sendwhatmsg(number, user_message, time_in_hour, time_in_minute)


def user_input_2():
  sleep(10)
  input_2 = input("\n\t[ℂ] Do you want to schedule another message? [Y/n]")
  if input_2 == "Y" or input_2 == "y":
    sleep(1)
    execute()

  elif input_2 == "n" or input_2 == "n":
    print("\n\t[ℂ] Returning to main-menu [ℂ]")
    sleep(1)
    bashCommand = "clear;. ./cyanide-framework.sh;main"
    output = subprocess.call(['bash','-c', bashCommand])

  else: 
    print("\n\t【X】wrong input!! Try Again【X】")
    screen_clear()
    sleep(1)
    user_input_2()

def executer():
  execute()
  user_input_2()
    

def user_input_3():
  screen_clear()
  print("\n")
  print(Fore.RED+"       ..,;:ccccccc:;...")
  print(Fore.WHITE+"    ..,clllc:;;;;;;:cllc,.")
  print(Fore.RED+"   .,cllc,..............';;'.")
  print(Fore.WHITE+"  .;lol;......"+Fore.WHITE+"_______"+Fore.RED+"....;lol;.")
  print(Fore.RED+" .,lol;......"+Fore.WHITE+"/ _____/"+Fore.RED+".....;lol;..  ")
  print(Fore.WHITE+" .coo......."+Fore.WHITE+"/ /"+Fore.RED+".............coo")
  print(Fore.RED+".'lol,....."+Fore.WHITE+"/ /"+Fore.RED+"............'lol,.")
  print(Fore.WHITE+".,lol,...."+Fore.WHITE+"/ /_____"+Fore.RED+"........,lol,.")
  print(Fore.RED+".,lol,...."+Fore.WHITE+"\______/"+Fore.RED+".......,lol,.")
  print(Fore.WHITE+" .:ooc'.................:ooc'")
  print(Fore.RED+"  .'cllc'.............cllc.")
  print(Fore.RED+ " [ 1  ] Schedule a message ")
  print(Fore.WHITE+ " [ 2  ] see all the messages sent ")
  print(Fore.RED+ " [ 3  ] clear logs ")
  print(Fore.WHITE+ "\n [ 99  ] Return to main-menu ")
  choice = int(input(Fore.RED+ "\n [ → ] Enter choice> : "))

  if choice == 1:
    executer()

  elif choice == 2:
    pywhatkit.showHistory()
    choice = input(" [ → ] Do you want to clear the logs? [Y/n] > : ")
    if choice == "Y" or choice == "y":
      f = open("pywhatkit_dbs.txt", "w")
      f.write("Woops! you have deleted the content! ")
      f.close()
      print(Fore.WHITE+Back.RED +"\n\tLogs cleared")
      sleep(1)
      user_input_3()

    elif choice == "n" or choice == "n":
      print("Returning Back")
      sleep(1)
      user_input_3()

    else:
      print("\n\t【X】wrong input!! TryAgain【X】")
      user_input_3()



  elif choice == 3:
    f = open("pywhatkit_dbs.txt", "w")
    f.write("No Logs ")
    f.close()
    print(Fore.WHITE + Back.RED+ "\n\tLogs cleared")
    sleep(1)
    user_input_3()

  elif choice == 99:
    print("\n\t[ℂ] Returning to main-menu [ℂ]")
    sleep(1)
    bashCommand = "clear;. ./cyanide-framework.sh;main"
    output = subprocess.call(['bash','-c', bashCommand])

  else:
    print("\n\t【X】wrong input!! Try Again【X】")


user_input_3()
