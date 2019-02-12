#!/usr/bin/python
#coding:utf-8

import sys, socket, argparse, random, requests

def get_joke():
	tmp = requests.get('http://chucknorrisfacts.fr/api/get?data=tri:alea;type:txt;nb:1').text
	joke = str(tmp.encode('utf8')).split('":"')[2].replace('","date', '').replace('&#039;', "'").replace('&eacute;', 'e').replace('&circ;', 'e').replace('&egrave;', 'e').replace('&agrave;', 'a').replace('&ocirc;', '')
	return joke

parser = argparse.ArgumentParser()
parser.add_argument("-p")
args = parser.parse_args()

host = '0.0.0.0'
port = int(args.p)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( (host, port) )

print "[+] Server is running on %s:%i" % (host, port)

while True:
    try:
        s.listen(5)
        conn, addr = s.accept()
        print "Received CLIENT: %s:%i" % (addr[0], addr[1])
        conn.send('Welcome to chat BOT !\n'.encode('utf8'))
        while True:
            data = conn.recv(1024)
            if len(data):
		data = data.decode('utf8').replace('\n', '')
                if data == 'cow':
			msg = "[COW]: MOUUUUUUUUUH\n\n"                	
		elif data == 'chuck':
			msg = "[BOT]: "+ get_joke() +" \n\n"
		elif data == 'exit':
			msg = "[BOT] Ok ciao !\n"
			conn.send(msg.encode('utf8'))
			conn.close()
		        s.close()
			sys.exit(0)
		else:
			msg = "[BOT]: Sorry master I'm confused\n\n"                
		conn.send(msg.encode('utf8'))
    except KeyboardInterrupt:
        print "\nClosing connection."
        conn.close()
        s.close()
        break

sys.exit(0)
