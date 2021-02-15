from scapy.all import *

#constants
SERVER_IP= '192.168.1.28'

msg = input("enter your message: ")
for ot in msg:
    dns_packet = IP(dst=SERVER_IP)/UDP(dport=ord(ot))/Raw(load="")
    send(dns_packet)

