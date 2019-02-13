#!/usr/bin/python
#coding: utf-8

#Import des modules
import socket,sys,datetime
date = datetime.datetime.now()

#Reponse
rage = '(╯°□°）╯︵ ┻━┻\n'
happy = '¯\_(ツ)_/¯\n'

#Definition des parametres
host = '127.0.0.1'
port = 1337

#Creation du socket
print '[+] Creating socket'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind du socket sur un port
print '[+] Binded on port %s' % port
s.bind((host, port))

#Le socket ecoute
print '[+] Now listenning...'
s.listen(5)

#On attend une connexion et si une connexion intervient, on l'accepte
while True:
    try:
        conn, addr = s.accept()
        welcome_date = ('Welcome \nWe are the %s and it is %s\nHow are you feeling today?\n') %(str(date)[:10],str(date)[11:16])
        conn.sendall (welcome_date)
        print ">>> Client connected: %s:%i" % (addr[0], addr[1])
        while True:
            data = conn.recv(1024)
            print data
            if data == "angry\n":
                conn.sendall (rage)
            elif data == "happy\n":
                conn.sendall (happy)
            elif data == "exit\n":
                conn.close()
                s.close
                print '[!] User closed the connection. Bye o/'
                sys.exit(1)
            else:
                conn.sendall ('How do you feel?\n')
    except KeyboardInterrupt:
        s.close()                       #Fermeture du socket
        print '[!] Bye o/'
        sys.exit(1)
