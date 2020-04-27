import os.path
import sys

def ip_file_valid():
    path = os.getcwd()
    print(path)

    #Use statis plain text file for IP addresses
    ip_file = path + "/ip.txt"

    #Checking if the file exists
    if os.path.isfile(ip_file) == True:
        print("\n IP File is valid :)\n")

    else:
        print("\n* File {} does not exist: ( Please check and try again.\n".format(ip_file))
        sys.exit()

    #Open user selected file for reading (IP Addresses file)
    selected_ip_file = open(os.path.join(sys.path[0], ip_file), 'r')

    #Starting from the beginning of the file
    selected_ip_file.seek(0)

    #Reading each line (IP address) in the file
    ip_list = selected_ip_file.readlines()

    #Closing the file
    selected_ip_file.close()

    return ip_list
