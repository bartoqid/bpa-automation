import sys
import getpass
from myfunctions.generate_dump import generate_dump
from myfunctions.ip_addr_valid import ip_addr_valid
from myfunctions.ip_reach import ip_reach
from myfunctions.ip_file_valid import ip_file_valid
from myfunctions.create_threads import create_threads, create_threads1
from myfunctions.generate_tsf import generate_tsf
from myfunctions.automated_bpa import automated_bpa


choice = input("Enter 1 for Stats Dump, Enter 2 for Tech Support File, Enter 3 for fully automated BPA submission (You need a BPA API Token) \nEnter 1,2,3:")
while (choice != '1') and (choice != '2') and (choice != '3'):
    choice = input("Dude, come one! Enter 1 for Stats Dump and Enter 2 for Tech Support File.\nEnter 1 or 2:")

# Enter username
firewall_admin = input("Please Enter firewall username: ")
# Enter password for firewall
firewall_password = getpass.getpass("Please enter firewall password: ")

if choice == '1':
    print("test")
    # Saving the list of ip address in in ip.txt to a variable
    ip_list = ip_file_valid()

    # verifying the validity of each ip address in the list
    try:
         ip_addr_valid(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    # Verifying the reachablity of each IP address in the list
    try:
        ip_reach(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    create_threads(ip_list, firewall_admin, firewall_password, generate_dump)

elif choice == '2':
    # Saving the list of ip address in in ip.txt to a variable
    ip_list = ip_file_valid()

    # verifying the validity of each ip address in the list
    try:
        ip_addr_valid(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    # Verifying the reachablity of each IP address in the list
    try:
        ip_reach(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    create_threads(ip_list, firewall_admin, firewall_password, generate_tsf)

elif choice == '3':

    token = input("Please Enter BPA API Token: ")

    # Saving the list of ip address in in ip.txt to a variable
    ip_list = ip_file_valid()

    # verifying the validity of each ip address in the list
    try:
        ip_addr_valid(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    # Verifying the reachablity of each IP address in the list
    try:
        ip_reach(ip_list)

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    create_threads1(ip_list, firewall_admin, firewall_password, token,  automated_bpa)
#End of program