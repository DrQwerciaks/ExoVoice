![Alt text](image.png)

# Przesyłanie Plików za pomocą Pythona

Ten projekt zawiera kod klienta i hosta napisany w Pythonie, który umożliwia przesyłanie plików z jednego komputera na drugi przez sieć. Klient pozwala użytkownikowi wybierać pliki do przesłania, a host odbiera te pliki i zapisuje je w bieżącym katalogu.

## Instrukcje

### Klient (client.py)

1. Uruchom plik `client.py` na komputerze, z którego chcesz przesłać plik.

2. W oknie interfejsu użytkownika kliknij przycisk "Wybierz plik", aby wybrać plik do przesłania.

3. Wybierz plik za pomocą okna dialogowego i potwierdź wybór.

4. Klient połączy się z hostem i przekaże wybrany plik.

### Host (host.py)

1. Uruchom plik `host.py` na komputerze, na którym chcesz odbierać pliki.

2. Host będzie oczekiwać na połączenie na określonym porcie (domyślnie port 12345).

3. Kiedy klient wybierze plik i nawiąże połączenie, host odbierze plik i zapisze go w bieżącym katalogu pod oryginalną nazwą.

## Wymagania

- Python 3.x

## Modyfikacje

### Dla hosta

- Możesz zmienić numer portu, na którym host nasłuchuje, zmieniając wartość zmiennej `listen_port`.

- Możesz dostosować zachowanie hosta w przypadku konfliktu nazw plików, np. nadpisać istniejący plik lub dodawać sufiks do nazwy.

### Dla klienta

- Możesz dostosować adres hosta i numer portu, do którego klient się łączy, zmieniając odpowiednio `server_host` i `server_port`.

## Autor

Ten projekt został stworzony przez [Twoje Imię i Nazwisko] (opcjonalne).

## Licencja

Ten projekt jest dostępny na licencji [MIT]. 

