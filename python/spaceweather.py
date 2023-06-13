from . import dependencies

# on some computers there seems to be an error with SSL handling, this should ensure secure connections over SSL
ssl._create_default_https_context = ssl._create_stdlib_context
# define all of our functions

def get_report():
    # set up the URL for the text file
    url = "https://services.swpc.noaa.gov/text/discussion.txt"
    
    # download the text file
    response = urllib.request.urlopen(url)
    report = response.read().decode()
    return report
    
def button1_click():
    report = get_report()
    report_section.config(state='normal')  # enable editing temporarily
    report_section.delete("1.0", tk.END)  # clear existing text
    report_section.insert(tk.END, report)  # insert the fetched report
    report_section.config(state='disabled')  # disable editing again
    
def get_sdo_Sun():
    
    #set up our variables, lists etc
    image_list = []
    url = f"https://sdo.gsfc.nasa.gov/assets/img/browse/{year}/{month}/{day}/"
    download_directory = "../images/sdo/"
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
        
    # download images with filenames containing "0304" and "4096"
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        pattern = re.compile(r'href="(.*?\.jpg)"')
        for match in pattern.finditer(html):
            filename = match.group(1)
            if "_0193" in filename and "_4096_" in filename and not "pfss" in filename and filename not in image_list:
            image_url = url + filename
            urllib.request.urlretrieve(image_url, download_directory + filename)
            print(f"Downloaded {filename}")

def get_soho_Sun():
