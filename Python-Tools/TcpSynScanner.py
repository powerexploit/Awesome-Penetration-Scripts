#!/usr/bin/python
#TcpSynScanner to check open port with syn scan
from scapy.all import *
ip = input("Enter the ip address or url:\n")
port = int(input("Enter the port number:\n"))
tcpRequest = IP(dst=ip)/TCP(dport=port,flags="S")
tcpResponse = sr1(tcpRequest,timeout=1,verbose=0)
if tcpResponse.getlayer(TCP).flags == "SA":
    print(port,"is listening")
else:
    print(port,"is not listening")
