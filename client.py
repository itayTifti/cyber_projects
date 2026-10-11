import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 1729))

message = "05WHORU"
client_socket.send(message.encode('utf-8'))

data = client_socket.recv(1024)
print(f"Received from server: {data.decode('utf-8')}")




