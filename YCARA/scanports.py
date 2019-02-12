#!/usr/bin/env python
# coding: utf-8
import socket
import subprocess
import sys
from datetime import datetime
from colorama import init
init()
from colorama import Fore

# Clear the screen
subprocess.call('cls', shell=True)

# Ask for input
# Victim scan : 192.168.35.97
remoteServer    = raw_input("Entrez une IP à scanner: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
start_scan      = input("Entrez un port de départ pour le scan: ")
fin_scan        = input("Entrez un port de fin pour le scan: ")
ports           = range(start_scan,fin_scan)

# Function to loop on ports
def loop_ports():
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            srv = socket.getservbyport(port)
            print "Port {}    ".format(port) + Fore.GREEN + "Ouvert" + Fore.RESET + '       Service : ' + srv
        else:
            print "Port {}: ".format(port) + Fore.RED + "Fermé" + Fore.RESET
        sock.close()

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Merci de patienter, scan en cours...", Fore.GREEN + remoteServerIP + Fore.RESET
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# We also put in some error handling for catching errors

try:
    loop_ports()

except KeyboardInterrupt:
    print "Combinaison Ctrl+C entrée"
    sys.exit()

except socket.gaierror:
    print "Impossible de résoudre l'hôte. Sortie du programme."
    sys.exit()

except socket.error:
    print "Erreur de création du socket"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scan Complété en: ', total
