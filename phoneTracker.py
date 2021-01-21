#!/usr/bin/env python3
import phonenumbers

country_code = input("Please enter the country code (eg. +91) :")
if len(country_code)<3 or len(country_code)>3:
    print("[X]Please enter valid country_code[x]")
    exit()
elif country_code[:1] != '+':
    print("Please enter correct country code: eg. +91")
    exit()

number = input("Please enter number :")
if len(number)<10 or len(number)>10:
    print("[X]Please enter a valid number[X]: eg.9876543210")
    exit()


mob_num = country_code + number
phoneN = phonenumbers.parse(mob_num)
print(phoneN)


#To get the country.
from phonenumbers import geocoder
#Here C stands for Country and H stands for History in "CH"
ch_number = phonenumbers.parse(mob_num, "CH")
geolocation = geocoder.description_for_number(ch_number, "en")
print("GeoLocation :")
print(geolocation)

#To know service provider.
from phonenumbers import carrier
service_number = phonenumbers.parse(mob_num, "SN")
service_provider = (carrier.name_for_number(service_number, "en"))
print("Service Provider :")
print(service_provider)

#To get the timmezone.
from phonenumbers import timezone
tz_num = phonenumbers.parse(mob_num, "TZ")
timeZone = timezone.time_zones_for_number(tz_num)
print("TimeZone :")
print(timeZone)

#To know whether the number is valid or not.
valid_num = phonenumbers.parse(mob_num)
validity = phonenumbers.is_valid_number(valid_num)
possible = phonenumbers.is_possible_number(valid_num)
print("Phone Number's Validity :")
print(validity)
print("Phone Number's Possibility :")
print(possible)
