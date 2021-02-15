from scapy.all import *


def is_without_data(packet):
    # print(packet['UDP'].len)
    if packet['UDP'].len is None:
        print(packet.show())
        print("worked!")
        return True
    return False


def is_udp(packet):
    # print(packet.show())
    if 'UDP' in packet:
        return True
    return False


def valid(packet):
    if is_udp(packet) and is_without_data(packet):
        return True
    return False


packets = sniff(count=1, lfilter = valid)
print(packets[0].show())
# print(packets[0]['UDP'].dport)



