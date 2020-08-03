#!/usr/bin/python3
import socket
import sys
host = "127.0.0.1"
port = 12345

# create a socket object
# AF_INET parameter is saying we are going to use a standard IPv4 address or hostname
# SOCK_STREAM indicates that this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((host,port))

# receive some data
response = client.recv(4096)

print(response)
client.close()
# close socket