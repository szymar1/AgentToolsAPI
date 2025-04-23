# Agent Tools API

Projekt API z dwoma narzędziami (tool1 i tool2) stworzony w FastAPI na potrzeby zadania Ag3nt Developer.

## Jak uruchomić lokalnie

1. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

2. Uruchom aplikację:

```bash
python main.py
```

3. Testuj endpointy:

- POST /tool1  
- POST /tool2

Payload:
```json
{
  "input": "UNIKAT"
}
```

## Deployment

Możesz użyć Render, Railway lub Heroku, aby opublikować API z publicznym dostępem HTTPS.
