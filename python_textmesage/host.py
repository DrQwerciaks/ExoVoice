import socket

# Serwer (host)
HOST = '127.0.0.1'  # Adres hosta
PORT_RANGE = range(1, 11)  # Zakres portów od 1 do 10

for PORT in PORT_RANGE:
    try:
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
    except Exception as e:
        print(f"Błąd na porcie {PORT}: {e}")
