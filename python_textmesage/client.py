import socket

# Klient
HOST = '127.0.0.1'  # Adres hosta serwera
PORT = 12345       # Port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        message = input("Wpisz wiadomość: ")
        client_socket.sendall(message.encode())
