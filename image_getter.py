import urllib.request
import os
import re

# get current date
from datetime import date
today = date.today()
year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")
path = './images/'

image_list = []

for filename in os.listdir(path):
    # check if the file extension is an image extension
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # if it is, add the filename to the list
        image_list.append(filename)

# specify url and download directory
url = f"https://sdo.gsfc.nasa.gov/assets/img/browse/{year}/{month}/{day}/"
download_directory = "./images/"

# create download directory if it doesn't exist
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# download images with filenames containing "0304" and "4096"
with urllib.request.urlopen(url) as response:
    html = response.read().decode()
    pattern = re.compile(r'href="(.*?\.jpg)"')
    for match in pattern.finditer(html):
        filename = match.group(1)
        if "0193" in filename and "4096" in filename and not "pfss" in filename and filename not in image_list:
            image_url = url + filename
            urllib.request.urlretrieve(image_url, download_directory + filename)
            print(f"Downloaded {filename}")
