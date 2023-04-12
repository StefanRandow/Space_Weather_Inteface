import urllib.request

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
    density = float(fields[7])
    speed = float(fields[8])
    temperature = str(fields[9])
    
    #returning values
    return speed, density, temperature
   
def get_report():
    # Set up the URL for the text file
    url = "https://services.swpc.noaa.gov/text/discussion.txt"
    
    # Download the text file
    response = urllib.request.urlopen(url)
    report = response.read().decode()
    return(report)
    

def main():

    #Present Options
    print("Welcome to the Space Weather Inteface, you have the following options:")
    print("1.) 1-Minute Averaged Real-time Bulk Parameters of the Solar Wind Plasma")
    print("2.) Space Weather Prediction Center Forecast Report")
    
    #Get User Choice
    choice = input("Enter a number corresponding to an option above: ")
    
    #printing values
    if choice == "1":
        speed, density, temperature = get_proton()
        
        if speed == -9999.9:
            print("ERROR")
        else:
            print("Speed: ", speed, "km/s")
            
        if density == -9999.9:
            print("ERROR")
        else:
            print("Density:", density, "protons/cm^3")
            
        if temperature == "-1.00e+05":
            print("ERROR")
        else:
            print("Temperature:", temperature, "K")
        
        input("Press Enter to continue...")
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
        
        
    elif choice == "2":
        report = get_report()
        print(report)
            input("Press Enter to continue...")
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
        
    else:
        print("Please try again")
        main()
    

    

main()
