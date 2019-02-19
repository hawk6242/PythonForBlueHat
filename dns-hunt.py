from collections import *
from scapy.all import *

packets = rdpcap("dns-tunnel-iodine.pcap")
#print(packets)
list = []

for pac in packets:
	if pac.haslayer("DNSRR"):
		if isinstance(pac.an, DNSRR):
			list.append(pac.an.rrname)
C = Counter(list)
print(len(C))
