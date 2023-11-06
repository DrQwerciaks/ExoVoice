import socket
import threading

# Host
HOST = '127.0.0.1'  # Adres hosta
PORT = 12345       # Port
MAX_CLIENTS = 10   # Maksymalna liczba klientów

clients = []

def handle_client(client_socket, addr, nick):
    clients.append((client_socket, nick))
    print(f"{nick} dołączył do czatu.")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"{nick} napisał: {message}")

            # Przesyłanie wiadomości do innych klientów
            for client, client_nick in clients:
                if client != client_socket:
                    client.send(f"{nick}: {message}".encode())
        except Exception as e:
            print(f"Błąd podczas obsługi klienta {nick}: {e}")
            break

    clients.remove((client_socket, nick))
    client_socket.close()
    print(f"{nick} opuścił czat.")

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
