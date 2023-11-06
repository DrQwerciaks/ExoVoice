import socket

# Klient
HOST = '127.0.0.1'  # Adres hosta serwera
PORT_RANGE = range(1, 11)  # Zakres portów od 1 do 10

nick = input("Podaj swój nick: ")

connected = False
for PORT in PORT_RANGE:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            connected = True
            while True:
                message = input(f"{nick} napisał: ")
                client_socket.sendall(f"{nick}: {message}".encode())
    except ConnectionRefusedError:
        print(f"Nie można połączyć się z portem {PORT}. Próbuję kolejny port...")
    except Exception as e:
        print(f"Błąd na porcie {PORT}: {e}")
    
    if connected:
        break

if not connected:
    print("Nie można nawiązać połączenia na żadnym z portów.")
