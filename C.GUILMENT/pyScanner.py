#!/usr/bin/python
#coding: utf-8
#import des modules necessaires
import socket, sys, subprocess, argparse
from datetime import datetime

# Clear le shell
subprocess.call('clear', shell=True)

# Parser d'argments
#Créer le parser
parser = argparse.ArgumentParser()
#Créer chaque argument en les indiquants comme obligatoire
parser.add_argument("-i", "--ip", help="IP Host", required=True)
parser.add_argument("-p", "--portmin",help="Port de scan minimum", required=True)
parser.add_argument("-P", "--portmax",help="Port de Scan maximum", required=True)
args = parser.parse_args()

# Gestion des variables depuis le parser
if args.ip:
	ip = args.ip
if args.portmin:
	port_started = int(args.portmin)
if args.portmax:
	port_ended = int(args.portmax)

#Vérification de la conformité de l'adresse IPv4

try:
	socket.inet_aton(ip)
except socket.gaierror:
	print "Adresse non valide"

#ASCII
print '''

                     $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ $$$$$$$$\ $$$$$$$\  
                    $$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |$$$\  $$ |$$  _____|$$  __$$\ 
 $$$$$$\  $$\   $$\ $$ /  \__|$$ /  \__|$$ /  $$ |$$$$\ $$ |$$$$\ $$ |$$ |      $$ |  $$ |
$$  __$$\ $$ |  $$ |\$$$$$$\  $$ |      $$$$$$$$ |$$ $$\$$ |$$ $$\$$ |$$$$$\    $$$$$$$  |
$$ /  $$ |$$ |  $$ | \____$$\ $$ |      $$  __$$ |$$ \$$$$ |$$ \$$$$ |$$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |$$\   $$ |$$ |  $$\ $$ |  $$ |$$ |\$$$ |$$ |\$$$ |$$ |      $$ |  $$ |
$$$$$$$  |\$$$$$$$ |\$$$$$$  |\$$$$$$  |$$ |  $$ |$$ | \$$ |$$ | \$$ |$$$$$$$$\ $$ |  $$ |
$$  ____/  \____$$ | \______/  \______/ \__|  \__|\__|  \__|\__|  \__|\________|\__|  \__|
$$ |      $$\   $$ |                                                                      
$$ |      \$$$$$$  |                                                                      
\__|       \______/        
						$$\    $$\         $$\       $$$$$$\  
						$$ |   $$ |      $$$$ |     $$$ __$$\ 
		> Autor : COBRAENCORNET		$$ |   $$ |      \_$$ |     $$$$\ $$ |
		> Date : 11/02/19		\$$\  $$  |        $$ |     $$\$$\$$ |
						 \$$\$$  /         $$ |     $$ \$$$$ |
						  \$$$  /          $$ |     $$ |\$$$ |
						   \$  /         $$$$$$\ $$\\$$$$$$  /
						    \_/          \______|\__|\______/ 
                                      
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

'''
try:
	# Demande à l'utilisateur l'ip
	#ip = raw_input("IP : ")
	# Affiche 60 fois le -
	print "-" * 60
	# Demande à l'utilisateur le port de depart
	#port_started = int(raw_input("Port de départ: "))
	# Demande à l'utilisateur le port de fin
	#port_ended = int(raw_input("Port de fin : "))
	# Récupère le nom de l'hote
	#host = socket.gethostbyaddr(ip)[0]
	# Initialise la variable port_open
	port_open = ""
	print "-" * 60
	print "-" * 60
	#print "Début du scan pour l'hôte " + host + " ip: " + ip
	print "-" * 60

	# Heure actuelle
	t1 = datetime.now()

	# Boucle for bouclant du premier au dernier port +1 (sinon s'arrete un port avant)
	for port in range(port_started, port_ended+1):
		# Creation du socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.01)
		# Connection à l'hote externe
		result = sock.connect_ex((ip, port))
		# Si le résultat = 0 cela veux dire que le port est ouvert
		if result == 0:
			# Affiche le port ouvert en vert
			print "[+] Port {}: 	 \033[32mOpen\033[0m".format(port) + "  	 " + socket.getservbyport(port)
			# Complète une variable de tous les ports ouverts
			port_open += "[+] Port {}: 	 \033[32mOpen\033[0m".format(port) + "  	 " + socket.getservbyport(port) + "\n"
		# Port fermer si autre résultat
		else:
			# Affiche le port fermer en rouge 
			print "[-] Port {}: 	 \033[31mClosed\033[0m".format(port)
		# Close la socket
		sock.close()

#Si le message d'erreur "KeyboardInterrupt" apparait print un autre message et quitte
except KeyboardInterrupt:
	print "Exit with CTRL + C"
	sys.exit()

# Heure actuelle
t2 = datetime.now()

# Calcul du temps d'éxécution du script
total =  t2 - t1
print "-" * 60
print '''
-----------------------------------
* RECAPITULATIF DES PORTS OUVERTS *
-----------------------------------
'''
#print "Host: %s" % host
print "IP: %s" % ip
print "-" * 20
# Print la liste de tous les ports ouvert
print port_open
print "-" * 60
# Affiche le temps d'exection
print "Scanner complété en : %s" % total
