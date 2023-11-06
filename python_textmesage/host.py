import socket

# Serwer (host)
HOST = '127.0.0.1'  # Adres hosta
PORT = 12345       # Port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Serwer nasłuchuje na porcie {PORT}...")
    conn, addr = server_socket.accept()
    with conn:
        print(f"Połączono z klientem {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Otrzymane dane: {data.decode()}")

    print("Serwer zakończył połączenie.")
