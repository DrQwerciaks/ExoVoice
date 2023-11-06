import websocket
import threading

# Adres serwera do komunikacji głosowej
server_address = "ws://localhost:5000/ws"  # Zmodyfikuj ten adres na odpowiedni dla swojego serwera

# Nazwa użytkownika
username = input("Podaj swoją nazwę użytkownika: ")

# Funkcja do obsługi odbieranych wiadomości
def on_message(ws, message):
    print(message)

# Funkcja do wysyłania wiadomości
def send_message(ws):
    while True:
        message = input()
        if message == "exit":
            break
        ws.send(message)

# Inicjalizacja klienta WebSocket
ws = websocket.WebSocketApp(server_address, on_message=on_message)
ws_thread = threading.Thread(target=ws.run_forever)
ws_thread.daemon = True
ws_thread.start()

# Wysyłanie wiadomości z klienta
send_thread = threading.Thread(target=send_message, args=(ws,))
send_thread.daemon = True
send_thread.start()

# Czekamy na zakończenie pracy klienta
ws_thread.join()
