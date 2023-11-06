import socket
import os

def receive_file(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(1)

        print(f"Oczekiwanie na połączenie na porcie {port}...")
        client_socket, client_address = server_socket.accept()
        print(f"Połączono z: {client_address}")

        # Odbierz pełną ścieżkę do pliku od klienta
        file_path = client_socket.recv(1024).decode()

        # Wyciągnij nazwę pliku z pełnej ścieżki
        file_name = os.path.basename(file_path)

        # Ustal bieżącą ścieżkę do pliku host.py
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Połącz ścieżkę do host.py z nazwą otrzymanego pliku
        file_path_on_server = os.path.join(current_directory, file_name)

        with open(file_path_on_server, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

        print(f"Plik otrzymany jako {file_name} i zapisany w {file_path_on_server}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    listen_port = 12345

    receive_file(listen_port)
