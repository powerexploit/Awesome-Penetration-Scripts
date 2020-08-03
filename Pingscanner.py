#!/usr/bin/python3
import sys
from scapy.all import *
def checkhost(ip):
	ping = IP(dst=ip)/ICMP()
	res = sr1(ping,timeout=1,verbose=0)
	if res == None :
		print("This host is down")
	else:
		print("This host is up")