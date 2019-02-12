# coding: utf-8
# python 3.7.1 x86_64

import socket
import sys

host = "127.0.0.1"
port = 4445
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[+] Creating socket")
s.bind(addr)
print(f"[+] Binding on port {port}")

s.listen()
print("[+] Now listening...")

while True:
    try:
        client, address = s.accept()
        client.sendall(b"Welcome !\n")
    except KeyboardInterrupt:
        print("[+] ...Bye")
        s.close()
        sys.exit(1)
    except Exception as err:
        print("[!] ...Error")
        s.close()
        sys.exit(2)

    while True:
        r = client.recv(2048).decode("utf-8").rstrip("\n")
        if r == "close":
            print("--> close receive")
            print("[+] ...Bye")
            client.sendall(b"bye")
            s.close()
            sys.exit(0)
        elif r == "perceval":
            client.sendall(b"c'est pas faux !\n")
        else:
            print(f"--> receive {r}")
            client.sendall(b"Chut !\n")

sys.exit(0)
