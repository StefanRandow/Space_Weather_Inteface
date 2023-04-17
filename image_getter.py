import urllib.request
import os
import re

# get current date
from datetime import date
today = date.today()
year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")

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
        if "0304" in filename and "4096" in filename:
            image_url = url + filename
            urllib.request.urlretrieve(image_url, download_directory + filename)
            print(f"Downloaded {filename}")
