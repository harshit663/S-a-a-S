# -*- coding: utf-8 -*-
"""
Created on Wed May 23 05:01:08 2018

@author: prjve
"""

import socket 
import subprocess as sp
import getpass

print("/t/t/tWelcome to my Saas cloud services")
print("""
1. Create an Account to use the software
2. Already have an account  
3. Exit  
""")
ch = input("Enter your choice :- ")
    
server_ip = "192.168.43.3"
server_port = 1111

client_ip = ""
clientip_out  = sp.getstatusoutput("ifconfig | grep inet | head -1 | awk '{print $2}'")
if clientip_out[0] == [0]:
    client_ip = clientip_out[1]
else:
    print("Ckeck your internet connection ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

if ch == 1:
    task = 'create'
    task = task.encode('utf-8')
    uname = input("Enter your username :- ")
    pw = getpass.getpass("Enter your password :- ")
    buname = uname.encode('utf-8')
    bpw = pw.encode('utf-8')
    soft = ("Enter the name of the software :- ")
    bsoft = soft.endcode('uft-8')
    print("Creating account in the server...")
    s.sendto(task, (server_ip, server_port))
    s.sendto(buname, (server_ip, server_port))
    s.sendto(bpw, (server_ip, server_port))
    s.sendto(bsoft, (server_ip, server_port))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    port1 = 2222
    s.bind((client_ip, port1))

    status = s.recvfrom(20)
    status = status[0].decode()
    
    if status == 'success':
        print("Account created successfully")
        sshpass = sp.getstatusoutput("echo y | yum isntall sshpass")
        saas_out = sp.getstatusoutput("sshpass -p {} ssh -l {} 192.168.43.3 -X {}".format(pw, uname, soft))
        
elif ch == 2:
    task = 'access'
    task = task.encode('utf-8')
    uname = input("Enter your username :- ")
    buname = uname.encode('utf-8')    
    passwd = getpass.getpass("Enter your password :- ")
    bpass = passwd.encode('utf-8')
    
    soft = ("Enter the name of the software :- ")
    bsoft = soft.endcode('uft-8')
    
            
        
        
        
    