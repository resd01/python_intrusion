# coding: utf-8
# python 3.7.1 x86_64

import socket
import sys

__author__ = "Maillard Alexandre"

host = "127.0.0.1"
port = 4445
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)

while True:
    reception = s.recv(4096).decode("utf-8").split("\n")

    for line in reception:
        if line == "Welcome !":
            print(f"[+] connection to {host}:{port} OK")
            print(line)
        elif line == "bye":
            print("[+] session close")
            s.close()
            sys.exit(0)
        elif len(line) > 0:
            print(f"--> {line}")
        else:
            msg = input(">>> ")
            s.sendall(msg.encode("utf-8"))

s.close()
