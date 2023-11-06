Projekt VoiceChat Python to przykład prostego systemu komunikacji głosowej między klientami za pomocą gniazd sieciowych. Ten projekt demonstrowany jest w języku Python i używa podstawowych bibliotek do komunikacji sieciowej.

## Funkcje

- Serwer (host) nasłuchuje na określonym porcie i obsługuje połączenia od klientów.
- Klienci łączą się z serwerem za pomocą adresu IP i portu serwera.
- Klienci mogą wysyłać i odbierać wiadomości tekstowe.
- Projekt może być rozwijany, aby obsługiwać bardziej zaawansowaną komunikację audio i video.




# Prosty przykład komunikacji między klientami w Pythonie

Ten prosty przykład pokazuje, jak można stworzyć dwóch klientów w języku Python, z których jeden działa jako serwer (host), a drugi jako klient, który łączy się z serwerem, aby komunikować się między sobą.

## Jak to działa

1. Klient Host (Serwer):
   - Uruchamiamy klienta hosta, który nasłuchuje na określonym porcie (np. 5000).
   - Klient hosta oczekuje na połączenie od klienta docelowego.
   - Gdy klient docelowy się połączy, mogą razem komunikować się poprzez gniazdo.

2. Klient Docelowy:
   - Uruchamiamy klienta docelowego, który łączy się z adresem IP i portem serwera hosta.
   - Po nawiązaniu połączenia, klient docelowy może wysyłać i odbierać wiadomości od klienta hosta.

## Instrukcje

1. Uruchom klienta hosta (serwera):
   ```bash```
   python host.py

##Uruchom klienta docelowego:

`bash`
Copy code
python client.py
Klient docelowy zostanie połączony z klientem hosta.

Teraz możesz wprowadzać wiadomości w kliencie docelowym, a będą one wysyłane do klienta hosta, który je odbierze i wyświetli.

##Wymagania
Python (zalecana wersja 3.x)

##Uwagi
Ten przykład jest bardzo uproszczony i służy tylko do celów demonstracyjnych. W rzeczywistości, w bardziej zaawansowanym scenariuszu, warto byłoby dodać obsługę wielu klientów, obsługę błędów i inne funkcje zwiększające niezawodność i funkcjonalność aplikacji.

Przykład ten używa modułu socket do obsługi komunikacji między klientami. W rzeczywistych projektach warto również rozważyć użycie bibliotek i frameworków do obsługi komunikacji sieciowej.

Pamiętaj, aby dostosować porty i adresy IP w kodzie, jeśli są inne niż te użyte w przykładzie.
