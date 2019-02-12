#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Import modules
import socket, time, sys, os
import argparse

from datetime import datetime
from termcolor import colored, cprint

parser = argparse.ArgumentParser(description='python script to scan a host')

parser.add_argument('-H', action='store', dest='host', help='Host to scan')
parser.add_argument('-s', action='store', dest='port_start', help='First port to scan', type=int)
parser.add_argument('-e', action='store', dest='port_end', help='Last port to scan', type=int)
parser.add_argument('-v', dest='verbose', help='Show all ports scanned', action="store_true")
args = parser.parse_args()

# Définition des paramètres
if args.host is None:
	host = raw_input('Host: ')
else:
	host = args.host

try:
    socket.inet_aton(host)
except socket.error:
	print ">>> Please, use correct ip address."
	sys.exit(1)

if args.port_start is None:
	port_start = int(raw_input('Start port: '))
else:
	port_start = args.port_start
if args.port_end is None:
	port_end = int(raw_input('End port: '))
else:
	port_end = args.port_end

if port_end < port_start:
	print ">>> The end port is lower thant the start one."
	sys.exit(2)
	pass

os.system('clear')

print unicode("╔", 'utf-8') + unicode("═", 'utf-8') * 78 + unicode("╗", 'utf-8')
print unicode("║", 'utf-8') + "                        _,.--.                                                " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "    --..,_           .'`__ o  `;__, nMap                                      " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "       `'.'.       .'.'`  '---'`  ' v1                                        " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "          '.`-...-'.'                                                         " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "            `-...-'                                                           " + unicode("║", 'utf-8')
print unicode("╚", 'utf-8') + unicode("═", 'utf-8') * 78 + unicode("╝", 'utf-8')
time_start = time.time()
# Bind du socket avec les paramètres
for x in xrange(port_start,port_end + 1):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.1)
	result = s.connect_ex((host, x))
	if result == 0:
		cprint("[+]\tPort open  : " + str(x) + "\t\t" + socket.getservbyport(x).rstrip(), 'green') 
	else:
		if args.verbose:
			cprint("[-]\tPort close : " + str(x), 'red')
			pass
	pass
	s.close()

print "> Done within %ss" % str(time.time() - time_start)
sys.exit(0)