import socket
import threading

# Serwer (host)
HOST = '127.0.0.1'  # Adres hosta
PORT_RANGE = range(1, 11)  # Zakres portów od 1 do 10

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data.decode())

for PORT in PORT_RANGE:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            print(f"Serwer nasłuchuje na porcie {PORT}...")
            while True:
                conn, addr = server_socket.accept()
                print(f"Połączono z klientem {addr}")
                client_thread = threading.Thread(target=handle_client, args=(conn,))
                client_thread.start()
    except Exception as e:
        print(f"Błąd na porcie {PORT}: {e}")
