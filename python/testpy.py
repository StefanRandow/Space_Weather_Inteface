import urllib.request
import os
import re
import calendar

#on some computers there seems to be an error with SSL handling, this should ensure secure connections over SSL
import ssl; ssl._create_default_https_context = ssl._create_stdlib_context

# get current date
from datetime import date
today = date.today()
# year = today.strftime("%Y")
# month = today.strftime("%m")
# day = today.strftime("%d")
path = '../images/sdo/'
mlist = [4, 6, 9, 11]

print("Welcome to the SDO query function.")
print("You will now be prompted to select a date to query.")
print("Please enter a year from the range: 2010 -",today.strftime("%m"))
year = int(input("Year: "))

print("Please enter a month from the range: 1 - 12")
month = int(input("Month: "))


if month in mlist:
    print(calendar.month_name[month]," has 30 days, please select a day from 1 - 30")
    day = input("Day: ")

elif month != 2:
    print(calendar.month_name[month]," has 31 days, please select a day from 1 - 31")
    day = input("Day: ")

else:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        # leap year checker
        print(calendar.month_name[month]," has 29 days, please select a day from 1 - 29")
        day = input("Day: ")
    else:
        print(calendar.month_name[month]," has 28 days, please select a day from 1 - 28")
        day = input("Day: ")

# end date selection criteria
print("You have selected: ", day, " ", calendar.month_name[month], "", year)
input("Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

#begin resolution criteria
print("Welcome to the SDO query function.")
print("You will now be prompted to select a resolution, and an wavelength to query.")
print("Please select from the available resolutions: \n512, 1024, 2048, 4096")
resolution = int(input("Resolution: "))

#begin resolution criteria
print("You will now be prompted to select a resolution, and a wavelength to query.")
print("Please select from the available wavelength (Angstroms): \n094, 131, 171, 193, 211, 304, 335, ")
wavelength = int(input("Wavelength: "))