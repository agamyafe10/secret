from scapy.all import *


def is_without_data(packet):
    """checking if the pacekts includes data for insuring this is the packet we want

    Args: packet (packet):

    Returns: true if there is no data else return false
    """
    if packet['UDP'].len == 8:# length 8 is the equivilent length for no data
        return True
    return False


def is_udp(packet):
    """checks if the packet is UDP

    Args: packet (packet)

    Returns: true if udp else false
    """
    if 'UDP' in packet:
        return True
    return False


def valid(packet):
    """checks if the packet is the one we want

    Args: packet (packet)

    Returns: true if stands the conditions else false
    """
    if is_udp(packet) and is_without_data(packet):
        return True
    return False


print("Started Sniffing...")
print("The message is: ")
while True:# keep sniffing because we have no length limit
    packets = sniff(count=1, lfilter = valid)# gets the wanted packet
    print(chr(packets[0]['UDP'].dport), end = "")# prints the letter according to the port the packets was sent to



