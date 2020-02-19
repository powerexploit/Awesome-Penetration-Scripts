#!/usr/bin/python3
import socket
import sys
host = sys.argv[1]
port = sys.arv[2]
# create a socket object
# AF_INET parameter is saying we are going to use a standard IPv4 address or hostname
# SOCK_DGRAM indicates that this will be a TCP client
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# send some date
client.sendto(b'aaaabbbccc',(host,port))

# receive some data
data,addr = client.recvfrom(1024)

print(data)

client.close()
# close socket