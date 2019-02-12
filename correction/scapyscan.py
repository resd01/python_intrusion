import time
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

ip = raw_input("Target addr >> ")
closed = 0
openp = []


def isTargetUp(addr):
    icmp = IP(dst=ip) / ICMP()
    ip = IP()
    ip.dst = addr
    resp = sr1(icmp, timeout=10)
    if resp == None:
        return False
    else:
        return True


conf.verb = 0
start_time = time.time()
port_min = int(raw_input("Port min: "))
port_max = int(raw_input("Port max: ")conf) + 1
ports = range(port_min, port_max)


if isTargetUp(ip):

    print "Host %s is up, start scanning" % ip

    for port in ports:

        srcPort = RandShort()
        synPacket = IP(dst=ip) / TCP(sport=srcPort, dport=port, flags='S')
        resp = sr1(synPacket, timeout=2)

        if resp:
            if resp.haslayer(TCP):
                if resp.getlayer(TCP).flags == 0x12:
                    print("[+] Port %s is open" % port)
                else:
                    print("[-] Port %s is closed" % port)
        else:
            print("[-] Port %s is closed" % port)
    duration = time.time() - start_time
    print "%s Scan Completed in %fs" % (ip, duration)
