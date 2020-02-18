import socket
host = "www.google.com"
port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((host,port))

# send some data
client.send(b"GET / HTTP/1.1Host : google.com")

# receive some data
response = client.recv(4096)

print(response)