import tkinter as tk
import urllib.request
import os
import re
import ssl
import cv2
import shutil

from PIL import Image, ImageTk
from datetime import date

# on some computers there seems to be an error with SSL handling, this should ensure secure connections over SSL
ssl._create_default_https_context = ssl._create_stdlib_context

# make sure we have an agreed working directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
# define all of our functions

def get_report():
    # set up the URL for the text file
    url = "https://services.swpc.noaa.gov/text/discussion.txt"
    
    # download the text file
    response = urllib.request.urlopen(url)
    report = response.read().decode()
    return report
    
def get_sdo_Sun():
    # set up our variables, lists, etc.
    image_list = []
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    url = f"https://sdo.gsfc.nasa.gov/assets/img/browse/{year}/{month}/{day}/"
    path = '../images/sdo/'

    # fill out the list so we don't get duplicates
    for filename in os.listdir(path):
        # check if the file extension is an image extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # if it is, add the filename to the list
            image_list.append(filename)

    # download images with filenames containing "HMIB" and "4096"
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        pattern = re.compile(r'href="(.*?\.jpg)"')
        for match in pattern.finditer(html):
            filename = match.group(1)
            if "_HMIB" in filename and "_4096_" in filename and not "pfss" in filename and filename not in image_list:
                image_url = url + filename
                urllib.request.urlretrieve(image_url, path + filename)
                print(f"Downloaded {filename}")
    # set up our variables, lists, etc.
    image_list = []
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    url = f"https://sdo.gsfc.nasa.gov/assets/img/browse/{year}/{month}/{day}/"
    path = '../images/sdo/'

    # fill out the list so we don't get duplicates
    for filename in os.listdir(path):
        # check if the file extension is an image extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # if it is, add the filename to the list
            image_list.append(filename)

    # download images with filenames containing "HMIB" and "4096"
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        pattern = re.compile(r'href="(.*?\.jpg)"')
        for match in pattern.finditer(html):
            filename = match.group(1)
            if "_HMIB" in filename and "_4096_" in filename and not "pfss" in filename and filename not in image_list:
                image_url = url + filename
                urllib.request.urlretrieve(image_url, path + filename)
                print(f"Downloaded {filename}")
    
    #set up our variables, lists etc
    image_list = []
    url = f"https://sdo.gsfc.nasa.gov/assets/img/browse/{year}/{month}/{day}/"
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    path = '../images/sdo/'
    
    # fill out the list so we dont get duplicates
    for filename in os.listdir(path):
    # check if the file extension is an image extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # if it is, add the filename to the list
            image_list.append(filename)
        
    # download images with filenames containing "HMIB" and "4096"
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        pattern = re.compile(r'href="(.*?\.jpg)"')
        for match in pattern.finditer(html):
            filename = match.group(1)
            if "_HMIB" in filename and "_4096_" in filename and not "pfss" in filename and filename not in image_list:
                image_url = url + filename
                urllib.request.urlretrieve(image_url, download_directory + filename)
                print(f"Downloaded {filename}")

def get_soho_Sun():
    # set up our variables, lists, etc.
    image_list = []
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    url = "https://umbra.nascom.nasa.gov/pub/incoming/lasco/rtmovie_png/"
    path = "../images/soho/"

    # fill out the list so we don't get duplicates
    for filename in os.listdir(path):
        # check if the file extension is an image extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # if it is, add the filename to the list
            image_list.append(filename)

    # download images with filenames containing the date and "c2"
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        pattern = re.compile(r'href="(.*?\.png)"')
        for match in pattern.finditer(html):
            filename = match.group(1)
            if date in filename and "c2" in filename and filename not in image_list:
                image_url = url + filename
                urllib.request.urlretrieve(image_url, path + filename)
                print(f"Downloaded {filename}")
    
    #set up our variables, lists etc
    image_list = []
    url = f"https://umbra.nascom.nasa.gov/pub/incoming/lasco/rtmovie_png/"
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    path = '../images/soho/'
    
    # fill out the list so we dont get duplicates
    for filename in os.listdir(path):
    # check if the file extension is an image extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # if it is, add the filename to the list
            image_list.append(filename)
        
    # download images with filenames containing "HMIB" and "4096"
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        pattern = re.compile(r'href="(.*?\.png)"')
        for match in pattern.finditer(html):
            filename = match.group(1)
            if date in filename and "c2" in filename and filename not in image_list:
                image_url = url + filename
                urllib.request.urlretrieve(image_url, download_directory + filename)
                print(f"Downloaded {filename}")

def sdo_Movie():
    
    #set up our vars, lists, etc
    
    folder_path = "../images/sdo/"
    files = os.listdir(folder_path)
    frames = []
    
    #sort files so they are alphabetical
    files.sort()
    
    # loop through all the files and add each image as a frame
    for file in files:
        # make sure we're only processing image files
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            # read in the image using OpenCV and add it to the frames list
            img = cv2.imread(os.path.join(folder_path, file))
            frames.append(img)
            
    # get the dimensions of the first frame to use for the output video
    height, width, channels = frames[0].shape
    # create a VideoWriter object to write the output video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # use XVID codec for AVI format
    out = cv2.VideoWriter('sdo.avi', fourcc, 24.0, (width, height), isColor=True)
    
    # write each frame to the output video
    for frame in frames:
        out.write(frame)
        
        # release the VideoWriter object and close all windows
    out.release()
    cv2.destroyAllWindows()
    
    # Set the original output file path
    original_path = 'sdo.avi'

    # Set the new output file path
    new_path = '../images/sdo.avi'

    # Move the file to the new location
    shutil.move(original_path, new_path)

def soho_Movie():
    
    #set up our vars, lists, etc
    
    folder_path = "../images/soho/"
    files = os.listdir(folder_path)
    frames = []
    
    #sort files so they are alphabetical
    files.sort()
    
    # loop through all the files and add each image as a frame
    for file in files:
        # make sure we're only processing image files
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            # read in the image using OpenCV and add it to the frames list
            img = cv2.imread(os.path.join(folder_path, file))
            frames.append(img)
            
    # get the dimensions of the first frame to use for the output video
    height, width, channels = frames[0].shape
    # create a VideoWriter object to write the output video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # use XVID codec for AVI format
    out = cv2.VideoWriter('sdo.avi', fourcc, 24.0, (width, height), isColor=True)
    
    # write each frame to the output video
    for frame in frames:
        out.write(frame)
        
        # release the VideoWriter object and close all windows
    out.release()
    cv2.destroyAllWindows()
    
    # Set the original output file path
    original_path = 'soho.avi'

    # Set the new output file path
    new_path = '../images/soho.avi'

    # Move the file to the new location
    shutil.move(original_path, new_path)


    window.config(bg = 'SystemButtonFace')

def main():
    
    #this function contains our main window
    # lets add some functions to the window
    def dark_Mode():
        window.configure(bg = '#14171f')
        report_section.configure(bg = '#2c313d')
        report_section.configure(fg = '#b3b3b3')
        fetch_Report.configure(bg = '#2c313d')
        fetch_Report.configure(fg = '#b3b3b3')
        
    def light_Mode():
        window.configure(bg = 'SystemButtonFace')
        report_section.configure(bg = 'SystemWindow')
        report_section.configure(fg = '#000000')
        fetch_Report.configure(bg = 'SystemWindow')
        fetch_Report.configure(fg = '#000000')

    def fill_Report():
        report_section.delete("1.0", tk.END) # this will clear the content
        content = get_report()
        report_section.configure(state = 'normal')
        report_section.insert(tk.END, content)
        report_section.configure(state = 'disabled')
    
   
    # okay lets set up our gui window
    icon_path = "../images/icon/icon.ico"
    window = tk.Tk()
    window.geometry("1376x768")
    window.title("Space Weather Interface GUI")
    window.iconbitmap(icon_path)

    # set up a menu bar accross the top
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    # add a "file" dropdown menu && the exit option
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_cascade(label="Exit", command = window.quit)

    # add a view button to the menu bar
    # add a "file" dropdown menu && the exit option
    view_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="View", menu=view_menu)

    view_menu.add_cascade(label="Dark Mode", command = dark_Mode)
    view_menu.add_cascade(label="Light Mode", command = light_Mode)

    # okay now lets make my text box
    report_section = tk.Text(window, state='disabled', width = 80, height = 20)
    report_section.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

    # okay fire! now lets make a button that pulls the report
    fetch_Report = tk.Button(window, text='Daily Forecast Report', command = fill_Report)
    fetch_Report.grid(row=2, column=0)

    window.mainloop()
    
if __name__ == '__main__':
    main()