import socket
import datetime
import random

def handle_client():
    client_socket, client_address = server.accept()
    print(f"connected to {client_address}")

    connected = True
    while connected:

        raw_data = client_socket.recv(2)
        if not raw_data:
            message = "Error - invalid commend"
            client_socket.sendall(message.encode('utf-8'))
            continue

        data_length = int(raw_data.decode("utf-8"))
        data = client_socket.recv(data_length+2).decode('utf-8')

        print(f"Received message: {data}")

        if data == "EXIT":
            connected = False
            print("connection stopped.")
            client_socket.close()

        elif data == "TIME":
            time = datetime.datetime.now()
            time = str(time)
            client_socket.sendall(time.encode('utf-8'))

        elif data == "WHORU":
            message = "A WORKING SERVER"
            client_socket.sendall(message.encode('utf-8'))

        elif data == "RAND":
            num = str(random.randint(1, 10))
            client_socket.sendall(num.encode())

        else:
            message = "Error - invalid commend"
            client_socket.sendall(message.encode('utf-8'))


def start_server():

    server.listen()
    print("Server is listening...")
    handle_client()


PORT = 1729
SERVER = "127.0.0.1"
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
start_server()

