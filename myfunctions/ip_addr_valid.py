import sys

#Checking octets
def ip_addr_valid(list):

    for ip in list:
            ip = ip.rstrip("\n")
            octet_list = ip.split(".")

            if(len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
                continue

            else:
                print("\n* There was an invalid IP address in the file: {} :(\n".format(ip))
                sys.exit()