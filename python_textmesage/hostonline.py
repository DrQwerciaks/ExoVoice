import socket
import threading

# Parametry serwera
HOST = '0.0.0.0'    # Adres hosta (dostępny dla wszystkich interfejsów)
PORT = 12345         # Port serwera
MAX_CLIENTS = 10     # Maksymalna liczba klientów
clients = []

def handle_client(client_socket, addr, nick):
    # Obsługa klienta, np. odbieranie i przesyłanie danych audio
    pass

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CLIENTS)

    print(f"Serwer nasłuchuje na porcie {PORT}...")

    while True:
        client_socket, addr = server_socket.accept()
        nick = client_socket.recv(1024).decode()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr, nick))
        client_thread.start()

if __name__ == "__main__":
    main()
