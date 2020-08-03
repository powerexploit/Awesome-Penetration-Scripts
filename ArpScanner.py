#!/usr/bin/python3
# ArpScanner.py for entire subnet
from scapy.all import *
print("Scanning the whole network...")
for lsb in range(1,110):
    ip = "192.168.43." +str(lsb)
    arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
    arpResponse  = srp1(arpRequest,timeout=1,verbose=0)
    if arpResponse:
        print("IP: " + " " + arpResponse.psrc + " " + "MAC:" + " " + arpResponse.hwsrc +" " + "Subnet:" + " " + arpResponse.pdst)
