import threading
import random
import socket

quotes = ["Just do it", "Life shrink or expands in proportion to one's courage", "We need less than we think we need"]

def handle_client(client_socket):
    quote = random.choice(quotes)
    client_socket.send(quote.encode())
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("172.20.10.11", 8080))
server.listen(5)

while True:
    client, address = server.accept()
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()