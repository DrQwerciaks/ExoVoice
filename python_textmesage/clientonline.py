import socket

# Parametry klienta
HOST = 'adres_serwera'  # Adres zdalnego serwera
PORT = 12345            # Port serwera
nick = input("Podaj swój nick: ")

def send_audio_data(client_socket):
    # Przykładowa funkcja do wysyłania danych audio
    pass

def receive_audio_data(client_socket):
    # Przykładowa funkcja do odbierania danych audio
    pass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(nick.encode())

    while True:
        # Obsługa przesyłania i odbierania danych audio
        pass
