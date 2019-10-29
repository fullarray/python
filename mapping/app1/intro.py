from scapy.all import *

## rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('smtp.pcap')

#Let's iterate through every packet
#for packet in packets:
#print(packet)
packets.summary()
