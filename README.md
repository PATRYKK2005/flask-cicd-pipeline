# Projekt 2 - docker compose

Aplikacja zbudowana jest we Flasku, połączona z bazą danych PostgreSQL przez SQLAlchemy. 
Całość uruchamiana przez Docker Compose jako dwa komunikujące się kontenery (web i db). 
Dane są trwałe dzięki Docker volumes.

## Wymagania
- Python 3.10+ i pip (do uruchomienia lokalnego)
- LUB Docker (do uruchomienia w kontenerze)

## Jak uruchomić lokalnie

1. Sklonuj repozytorium:
```bash
git clone https://github.com/PATRYKK2005/flask-docker-compose-up-database
cd flask-docker-compose-up-database
```

2. Stwórz i aktywuj wirtualne środowisko:
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac
```

3. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

4. Uruchom aplikację:
```bash
python app.py
```

5. Aplikacja będzie dostępna pod adresem `http://127.0.0.1:5000`


## Jak uruchomić przez Docker Compose

1. Stwórz plik `.env` na podstawie `.env.example` i uzupełnij wartości
2. Uruchom:
```bash
docker compose up --build
```
3. Aplikacja będzie dostępna pod `http://localhost:5000`

## Zmienne środowiskowe

Stwórz plik `.env` na podstawie `.env.example`:

| Zmienna | Opis |
|---------|------|
| `POSTGRES_USER` | Nazwa użytkownika bazy danych |
| `POSTGRES_PASSWORD` | Hasło do bazy danych |
| `POSTGRES_DB` | Nazwa bazy danych |
| `DATABASE_URL` | Pełny adres połączenia z bazą |

## Endpointy

| Endpoint | Metoda | Opis                                                                                |
|----------|--------|-------------------------------------------------------------------------------------|
| `/`      | GET    | Zwraca status serwera i aktualny czas w JSON                                        |
| `/baza`  | GET    | Zwraca obecne wpisy do bazy danych                                                  |
| `/baza`  | POST   | Dodaje nowe wpisy do bazy danych, wymagane pola: {"title": "...", "content": "..."} |

