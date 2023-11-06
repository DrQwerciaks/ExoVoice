import socket
import tkinter as tk
from tkinter import filedialog

def send_file(filename, host, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Przekaż nazwę pliku do serwera
        client_socket.send(filename.encode())

        with open(filename, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.send(data)

        print(f"Plik {filename} został przesłany na {host}:{port}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        client_socket.close()

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        send_file(file_path, server_host, server_port)

if __name__ == "__main__":
    server_host = "127.0.0.1" #Podaj adres IP host ( na które ma iść pliki)
    server_port = 12345 #nasłuchiwanie portów

    root = tk.Tk()
    root.title("Przesyłanie plików")

    browse_button = tk.Button(root, text="Wybierz plik", command=browse_file)
    browse_button.pack()

    root.mainloop()
