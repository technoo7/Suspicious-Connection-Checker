# This code is a Python script that checks for suspicious TCP network connections established by running 
# processes on the local machine. It uses the psutil library to get a list of all TCP connections and then 
# checks each connection to see if it is suspicious. A connection is considered suspicious if it meets any 
# of the following criteria:

# 1. It is an established connection that is not from localhost or private IPs.
# 2. It is established on a common backdoor port (e.g., 4444, 5555, 6666, or 31337).
# 3. The process associated with the connection has a suspicious name (e.g., "rat", "keylogger", or "backdoor").
# 4. The process is running from an unusual location.

# If a suspicious connection is found, the script outputs information about the connection, including the 
# local and remote addresses, the status, the process name, and the remote host name (if available).

def Main():
    print("░▒█▀▀▀█░▒█▀▀▄░▒█▀▀▄\n░░▀▀▀▄▄░▒█░░░░▒█░░░\n░▒█▄▄▄█░▒█▄▄▀░▒█▄▄▀")
    print("By Technobeast To Protect Your PC\n")
    while True:
        q = input("User > ")
        CommandHandler(q)

def CommandHandler(command):
    if command == "/help":
        print("This Program Checks For Suspicious TCP network connection established by running processes on the local machine just type /check\n")
    elif command == "/clear":
        os.system("cls")
    elif command == "/check":
        Animation()
        os.system("cls")
        
    elif command == "/quit":
        quit(1)
    else:
        print("Command Not Found Try pressing /help\n")

import psutil
import socket
import os
from time import sleep

def Animation():
    os.system("cls");print("Checking for suspicious connections.");sleep(0.1);os.system("cls");print("Checking for suspicious connections..");sleep(0.1);os.system("cls");print("Checking for suspicious connections...");sleep(0.1)
    os.system("cls");print("Checking for suspicious connections.");sleep(0.1);os.system("cls");print("Checking for suspicious connections..");sleep(0.1);os.system("cls");print("Checking for suspicious connections...");sleep(0.1)
    os.system("cls");print("Checking for suspicious connections.");sleep(0.1);os.system("cls");print("Checking for suspicious connections..");sleep(0.1);os.system("cls");print("Checking for suspicious connections...");sleep(0.1)
    os.system("cls")
    check_suspicious_connections(connections = psutil.net_connections(kind='tcp'))
        

def check_suspicious_connections(connections):
    for conn in connections:
        # Check for established connections that are not from localhost or private IPs
        if conn.status == 'ESTABLISHED' and conn.raddr and not is_private_ip(conn.raddr[0]):
            # Check for common backdoor ports and suspicious processes
            if conn.raddr[1] in [4444, 5555, 6666, 31337] or is_suspicious_process(conn.pid):
                print('Suspicious Connection Detected:')
                print(f'Local address: {conn.laddr}')
                print(f'Remote address: {conn.raddr}')
                print(f'Status: {conn.status}')
                print(f'Process name: {psutil.Process(conn.pid).name()}')
                print(f'Remote host name: {get_host_name(conn.raddr[0])}')
                print("===================================================")

def is_private_ip(ip):
    # Check if the IP address is in the private range (RFC 1918)
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    if octets[0] == '10':
        return True
    if octets[0] == '172' and 16 <= int(octets[1]) <= 31:
        return True
    if octets[0] == '192' and octets[1] == '168':
        return True
    return False

def is_suspicious_process(pid):
    try:
        # Check if the process is running from an unusual location or has a suspicious name
        process = psutil.Process(pid)
        if process.exe() != process.cwd():
            return True
        if any(keyword in process.name().lower() for keyword in ['rat', 'keylogger', 'backdoor']):
            return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    return False

def get_host_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return ip
    
Main()