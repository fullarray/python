
#get libraries in the current environment

import scapy

from scapy.all import PcapReader

# rdpcap comes from scapy ands load in our pcap file

#packets = rdpcap('smtp.pcap')

# Let's iterate through every packet
#for packet in packets:
#    print(packet)
packets.summary()

with PcapReader('smtp.pcap') as pcap_reader:
 for pkt in pcap_reader:
     print (pkt)

# import pcapng
# from pcapng import FileScanner
# import sys
# 
# with open('scannet.pcap', 'rb') as fp:
#     scanner = pcapng.FileScanner(fp)
#     blocks = list(scanner)
#     for block in blocks:
#          print(block)
