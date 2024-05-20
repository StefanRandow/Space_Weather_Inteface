import cv2
import os
import shutil
import calendar
# get current date
from datetime import date
today = date.today()
# year = today.strftime("%Y")
# month = today.strftime("%m")
# day = today.strftime("%d")
mlist = [4, 6, 9, 11]

os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to the Movie Making function.")
print("Please begin by entering the satelite you wish to compile images from:")
sat = input("SDO or SOHO: ")
print("Please enter a year from the range: 2010 -",today.strftime("%Y"))
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
print("You will now be prompted to select a wavelength to compile.")
print("Please select from the available wavelength (Angstroms): \n094, 131, 171, 193, 211, 304, 335, ")
wavelength = int(input("Wavelength: "))

#begin resolution criteria
print("You will now be prompted to select a resolution to compile.")
print("Please select from the available resolutions: \n512, 1024, 2048, 4096")
resolution = int(input("Resolution: "))

# okay we are done with all the user input stuff, now we can actually execute.



# here we define some things we're about to use
image_list = []
folder_path = f"../images/{year}/{month}/{day}/{sat}/{wavelength}/{resolution}/"
name = f"{sat}{year}{month}{day}{wavelength}{resolution}.avi"

# get a list of all the files in the folder
files = os.listdir(folder_path)

# sort the files alphabetically to ensure the frames of the video are in order
files.sort()

# create a list to hold all the image frames
frames = []

# loop through all the files and add each image as a frame
for file in files:
    # make sure we're only processing image files
    if file.endswith(".jpg"):
        # read in the image using OpenCV and add it to the frames list
        img = cv2.imread(os.path.join(folder_path, file))
        frames.append(img)

# get the dimensions of the first frame to use for the output video
height, width, channels = frames[0].shape

# create a VideoWriter object to write the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # use XVID codec for AVI format
out = cv2.VideoWriter(name, fourcc, 24.0, (width, height), isColor=True)

# write each frame to the output video
for frame in frames:
    out.write(frame)

# release the VideoWriter object and close all windows
out.release()
cv2.destroyAllWindows()

# Set the new output file path
release_directory = f"../movies/{name}"

# Move the file to the new location
shutil.move(name, release_directory)

print("Your AVI has been generated and placed in the movies folder")