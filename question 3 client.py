import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.20.10.11", 8080))

quote = client.recv(1024).decode()
print("Quote of the Day: " + quote)

client.close()