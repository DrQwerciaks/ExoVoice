import socket

# Klient
HOST = '127.0.0.1'  # Adres hosta serwera
PORT = 12345       # Port

nick = input("Podaj swój nick: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(nick.encode())

    while True:
        message = input("Napisz wiadomość: ")
        client_socket.sendall(message.encode())
