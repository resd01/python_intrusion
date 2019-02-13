#!/usr/bin/python
#coding: utf-8

#Module imports
import sys, socket, subprocess, colorama
from colorama import Fore, Back, Style, init

art = '''
#############################
#                           #
#       Port Scan           #
#                           #
#############################
            ________   .==.
by cuicui  [________>c((_  )
                       '=='
'''

def joli():
    subprocess.call('clear', shell=True)
    print (art)

def known_port(port):
    with open("/etc/services") as search:
        for line in search:
            string_port = "\t" + str(port) + "/"
            line = line.rstrip()  # remove '\n' at end of line
            if string_port in line:
                return(line)

#Asking for parameters
joli()
target_ip = raw_input('Which target? (@IP)\n')
range_min = input('Enter the first port (starting at:)\n')
range_max = input('Enter the last port (finishing at:)\n')

#Starting the scan
joli()
print 'Starting scanning %s at port %s to %s' %(target_ip,range_min,range_max)
try:
    for port in range(range_min,range_max):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            if known_port(port):
                print ("Port: " + str(port) + Fore.GREEN + "\tOpen\t" + Fore.RESET + known_port(port))
            else:
                print ("Port: " + str(port) + Fore.GREEN + "\tOpen\t" + Fore.RESET)
        else:
            if known_port(port):
                print ("Port: " + str(port) + Fore.RED + "\tClosed\t" + Fore.RESET + known_port(port))
            else:
                print ("Port: " + str(port) + Fore.RED + "\tClosed\t" + Fore.RESET)
        sock.close()

#Handling exit
except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()
