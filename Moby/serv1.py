#!/usr/bin/python
#coding: utf-8
from threading import Thread
import socket, time, sys
from chuck import ChuckNorris

host = '127.0.0.1'
port = 1337

#Creation du socket
print '[+] Creating socket ...'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind du socket sur un port
print '[+] Binding socket ...'
s.bind((host, port))

#Le socket écoute
print '[+] Now listening ...'
s.listen(5)

#On attend une connexion et si une connexion intervient, on l'accepte
while True:
	try:
		conn, addr = s.accept()
		conn.sendall('Welcome\n')
		print ">>> Client connected : %s:%i" % (addr[0], addr[1])
		while True:
			cn = ChuckNorris()
			conn.send("C>")
			response = conn.recv(1024)
			if response != "":
				print response.rstrip()
				if response.rstrip() == "OSS":
					r='Comment est votre blanquette ?\n'
					conn.send(r)
				elif response.rstrip() == "Chuck Norris" or response.rstrip() == "Chuck" or response.rstrip() == "Norris":
					r=cn.random()
					conn.send(r.joke)
					conn.send("\n")
				elif response.rstrip() == "FIN":
					break
				else:
					r='Hello\n'
					conn.send(r)
				
	except KeyboardInterrupt:
		s.close()
		print '[+] Bye !'
		sys.exit(1)
