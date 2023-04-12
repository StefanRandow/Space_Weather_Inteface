import urllib.request
import os
def get_proton():
    # Set up the URL for the text file
    url = "https://services.swpc.noaa.gov/text/ace-swepam.txt"
    
    # Download the text file
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    
    # Split the text file into lines
    lines = data.split("\n")

    # Extract the most recent solar wind data from the second-to-last line
    last_line = lines[-2]
    fields = last_line.split()

    # Extract the solar wind speed, density, and temperature from the fields
    s = float(fields[6])
    density = float(fields[7])
    speed = float(fields[8])
    temperature = (fields[9])
    
    #returning values
    return s, speed, density, temperature
    
def get_gsm():
    # Set up the URL for the text file
    url = "https://services.swpc.noaa.gov/text/ace-magnetometer.txt"
    
    # Download the text file
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    
    # Split the text file into lines
    lines = data.split("\n")
    
    # Extract the most recent Interplanetary Magnetic Field data from the second-to-last line
    last_line = lines[-2]
    fields = last_line.split()
    
    # Extract the Bx, By, Bz, Bt data from the fields
    S =  float(fields[6])
    Bx = float(fields[7])
    By = float(fields[8])
    Bz = float(fields[9])
    Bt = float(fields[10])
    
    #return all collected values
    return S, Bx, By, Bz, Bt
   
def get_report():
    # Set up the URL for the text file
    url = "https://services.swpc.noaa.gov/text/discussion.txt"
    
    # Download the text file
    response = urllib.request.urlopen(url)
    report = response.read().decode()
    return(report)
    

def main():

    #Present Options
    print("Welcome to the Interplanetary Space Weather Inteface, \nThis data is collected by the Advanced Composition Explorer (ACE). \n\nYou have the following options: \n")
    print("1.) 1-Minute Averaged Real-time Interplanetary Solar Wind Plasma Data")
    print("2.) Space Weather Prediction Center Forecast Report")
    print("3.) 1-Minute Averaged Real-time Interplanetary Magnetic Field Data")
    
    #Get User Choice
    choice = input("Enter a number corresponding to an option above: ")
    
    #printing values
    if choice == "1":
    
        #clean up screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #update values
        s, speed, density, temperature = get_proton()
        
        #Print Information
        print("\nLatest data on Solar Wind Plasma (Protons) at the L1 Lagrange is below \n")
        
        #Account for Errors
        if s != 0:
            print("ERROR EITHER BAD DATA OR NO DATA \nTRY AGAIN IN 1 MINUTE")
        
        #print data
        else:
            print("Speed: ", speed, "km/s")
            print("Density: ", density, "protons/cm^3")
            print("Temperature: ", temperature, "K")
        
        #prepare for follow on mission
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
        
        
    elif choice == "2":
    
        #clean up screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        report = get_report()
        print("\n")
        print(report)
        print("\n")
        
        #prepare for follow on mission
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    
    elif choice == "3":
        
        #clean up screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\nLatest Data on Interplanetary Magnetic Field Values (GSM Coordinates): \n")
        S, Bx, By, Bz, Bt = get_gsm()
        
        if S != 0:
            print("ERROR EITHER BAD DATA OR NO DATA \nTRY AGAIN IN 1 MINUTE")
        
        else:
            print("Magnetic Field Strength in the X direction: ", Bx, "nT")
            print("Magnetic Field Strength in the Y direction: ", By, "nT")
            print("Magnetic Field Strength in the Z direction: ", Bz, "nT")
            print("Total Magnetic Field Magnitude: ", Bt, "nT \n")
        
        #prepare for follow on mission
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
        
    
    
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please try again")
        main()
    

    

main()
