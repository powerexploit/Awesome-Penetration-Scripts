#! /usr/bin/env python
# arping2tex : arpings a network and outputs

import sys
if len(sys.argv) != 2:
    print("Usage: arping2tex <net>\n  eg: arping2tex 192.168.1.0/24")
    sys.exit(1)

from scapy.all import srp,Ether,ARP,conf
conf.verb=0
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]),timeout=2)

for snd,rcv in ans:
    print(rcv.sprintf(r"%Ether.src% & %ARP.psrc%\\"))
