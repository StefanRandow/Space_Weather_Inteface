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
mlist = [4, 6, 9, 11]

print("Welcome to the SDO query function.")
print("You will now be prompted to select a date to query.")
print("Please enter a year from the range: 2010 -",today.strftime("%m"))
year = int(input("Year: "))

print("Please enter a month from the range: 1 - 12")
month = int(input("Month: "))


if month in mlist:
    print(calendar.month_name[month]," has 30 days, please select a day from 1 - 30")
    day = int(input("Day: "))

elif month != 2:
    print(calendar.month_name[month]," has 31 days, please select a day from 1 - 31")
    day = int(input("Day: "))

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
print("You will now be prompted to select a wavelength to query.")
print("Please select from the available wavelength (Angstroms): \n094, 131, 171, 193, 211, 304, 335, ")
wavelength = int(input("Wavelength: "))

#begin resolution criteria
print("You will now be prompted to select a resolution to query.")
print("Please select from the available resolutions: \n512, 1024, 2048, 4096")
resolution = int(input("Resolution: "))

# okay we are done with all the user input stuff, now we can actually execute.



# here we define some thinsg we're about to use
image_list = []
path = f"../images/{year}/{month}/{day}/sdo/{wavelength}/{resolution}/"
release_directory = "../movies/"

# create download directory if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path)

if not os.path.exists(release_directory):
    os.makedirs(release_directory)

for filename in os.listdir(path):
    # check if the file extension is an image extension
    if filename.lower().endswith(('.jpg')):
        # if it is, add the filename to the list
        image_list.append(filename)

# here we have to format the information so NASA doesn't hate us :/
if month < 10:
    month = "0"+str(month)
    
if day < 10:
    day = "0"+str(day)
    
if wavelength < 1000:
    wavelength = "0"+str(wavelength)

# specify url and download directory
url = f"https://sdo.gsfc.nasa.gov/assets/img/browse/{year}/{month}/{day}/"


# download images with filenames containing "wavelength" and "resolution"
with urllib.request.urlopen(url) as response:
    html = response.read().decode()
    pattern = re.compile(r'href="(.*?\.jpg)"')
    for match in pattern.finditer(html):
        filename = match.group(1)
        if "_"+str(wavelength)+"." in filename and "_"+str(resolution)+"_" in filename and not "pfss" in filename and filename not in image_list:
            image_url = url + filename
            urllib.request.urlretrieve(image_url, path + filename)
            print(f"Downloaded {filename}")
