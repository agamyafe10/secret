from scapy.all import *
import time

#constants
SERVER_IP= '0.0.0.0'

msg = input("enter your message: ")
# The code makes a delay between each packet sent in order to avoid missing or confusion of 
# packets in the server(let the server more time
#  to proccess so he manages to recieve all of the packets)
for ot in msg:
    dns_packet = IP(dst=SERVER_IP)/UDP(dport=ord(ot))/Raw(load="")# build the packet with destenation port according to the letter asci value
    send(dns_packet)
    time.sleep(1)