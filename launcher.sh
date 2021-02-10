#!/usr/bin/env bash

[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo  $red "You must be root to run the script"; echo ; exit 1; }


clear

pwd=$(pwd)

cd $pwd
. ./cyanide-framework.sh;checkinternet
. ./cyanide-framework.sh;check_os
. ./cyanide-framework.sh;check_dependencies
. ./cyanide-framework.sh;lading_bar
# . ./cyanide-framework.sh;banner
. ./cyanide-framework.sh;main
