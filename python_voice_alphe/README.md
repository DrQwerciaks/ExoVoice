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
