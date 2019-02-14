#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime





subprocess.call('clear', shell=True)

ART = '''
   ___       _   _                 
  / _ \_   _| |_| |__   ___  _ __  
 / /_)/ | | | __| '_ \ / _ \| '_ \ 
/ ___/| |_| | |_| | | | (_) | | | |
\/     \__, |\__|_| |_|\___/|_| |_|
       |___/                       
       
    > Author : MLF
--------------------------------------------
'''

print ART


remoteServer    = raw_input("Adresse IP de la machine distante: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

startPort = raw_input("Entrer le premier port a scanner: ")
endPort = raw_input("Entrer le dernier port a scanner: ")

print "-" * 60
print "Scan en cours sur %s" % remoteServerIP
print "-" * 60

# Debut du scan
t1 = datetime.now()


try:
    for port in range(int(startPort),int(endPort)):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "[+] Port %i:\t\tOpen		%s" % (port, socket.getservbyport(port))
	else:
	    print "[-] Port %i:\t\tClose" % port
        sock.close()

except KeyboardInterrupt:
    print "Bye"
    sys.exit()

except socket.gaierror:
    print 'Adresse IP incorrect'
    sys.exit()

except socket.error:
    print "Impossible de se connecter"
    sys.exit()

# Fin du scan
t2 = datetime.now()

# Calcul de la duree du scan
total =  t2 - t1

# Printing the information to screen
print 'Scan effectue en: %s' % total
