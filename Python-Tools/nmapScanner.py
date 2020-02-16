#!/usr/bin/python
import sys
try:
    import nmap
except:
    sys.exit("[!] install the nmap module: pip install python-nmap")
#argument validator
if len(sys.argv) !=3:
    sys.exit("Please provide two arguments first being target address & second being port")
ports = str(sys.argv[2])
addrs = str(sys.argv[1])

scanner = nmap.PortScanner()
scanner.scan(addrs,ports)
for host in scanner.all_hosts():
    if not scanner[host].hostname():
        print("The host ip address is %s and its hostname was not found" %(host))
    else:
        print("The host ip address is %s and its hostname is %s" %(host,scanner[host].hostname()))
